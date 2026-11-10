using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerPuckMovement : MonoBehaviour
{


    public PuckState currentState = PuckState.Hidden;
    
    public RectTransform playerPuck;
    public Vector2 puckOffset;
    public Vector2 lastMousePos;
    public float returnPuckAnimTime = 0.2f;
    private float returnPuckAnimElapsed = 0f;

    public void SetPuckState(int newState)
    {
        PuckState newStateEnum = (PuckState)newState;
        if (currentState == PuckState.Hidden && newStateEnum == PuckState.PickUp)
        {
            currentState = newStateEnum;
        }

        else if (currentState == PuckState.PutDown && newStateEnum == PuckState.ReturntoCursor)
        {
            currentState = newStateEnum;
        }

        else if (currentState == PuckState.PickUp && (newStateEnum == PuckState.PutDown || newStateEnum == PuckState.Hidden))
        {
            currentState = newStateEnum;
        }

    }


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Mouse.current.rightButton.wasPressedThisFrame)
        {
            SetPuckState(3);
        }
        switch (currentState)
        {
            case PuckState.Hidden:
                /*
                 * puck is not visible while mouse is not on character Grid -> SetActive-> false;
                 */
                playerPuck.gameObject.SetActive(false);

                break;


            case PuckState.PickUp:
                /* when hovering over character grid:
                    * get location of cursor -> Vector2 mousePos = Input.mousePosition;
                    * puck becomes visible above pointed finger (slightly above center) -> puck.IsActive? SetActive?
                    * puck continues to follow cursor with that offset -> in Update, continually set cursorPos to mousePos??
                    */
                playerPuck.gameObject.SetActive(true);
                Vector2 mousePos = Mouse.current.position.ReadValue();
                Debug.Log(mousePos);
                playerPuck.anchoredPosition = mousePos + puckOffset;
                lastMousePos = mousePos + puckOffset;
                break;

            case PuckState.PutDown:
                /*on click of cursor AND in valid character tile:
                 *  get location of click -> on click, stop tracking mousePos, and set that last known Pos to cursorPos?
                 *  puck leaves cursor
                 *  puck stays in click position RELATIVE to cursor offset
                 *  no more puck on cursor
                 */
                playerPuck.gameObject.SetActive(true);
                playerPuck.anchoredPosition = lastMousePos;
                break;

            case PuckState.ReturntoCursor:
                /* if character was selected but THEN deselected AND cursor is still in tile grid:
                 *     get cursor location
                 *     cursor animates in an arc to land on its place with the cursor
                 *     continues to follow cursor while hovering over character grid
                 */
                mousePos = Mouse.current.position.ReadValue() + puckOffset;
                Vector2 puckDownPos = lastMousePos;

                float animProgress = returnPuckAnimElapsed / returnPuckAnimTime;
                playerPuck.anchoredPosition = Vector3.Slerp(puckDownPos, mousePos, animProgress);
                returnPuckAnimElapsed += Time.deltaTime;

                if (animProgress >= 1)
                {
                    returnPuckAnimElapsed = 0;
                    currentState = PuckState.PickUp;
                }

                        
                break;

            default:
                break;
        }
    }
}
public enum PuckState
{
    Hidden,
    PickUp,
    PutDown,
    ReturntoCursor
}
