using UnityEngine;

public class PlayerCursor : MonoBehaviour
{
    [Header("Cursor Sprites")]
    public Texture2D defaultCursorImg;
    public Texture2D holdPuckCursorImg;
    public Texture2D noPuckCursorImg;

    public PlayerPuckMovement puckMovement;
    public Vector2 cursorOffset;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        Cursor.SetCursor(defaultCursorImg, new Vector2 (26,0), CursorMode.Auto);
    }

    // Update is called once per frame
    void Update()
    {
        if (puckMovement.currentState == PuckState.Hidden)
        {
            Cursor.SetCursor(defaultCursorImg, cursorOffset, CursorMode.Auto);
            //Debug.Log("hide it");
        }

        else if (puckMovement.currentState == PuckState.PickUp)
        {
            Cursor.SetCursor(holdPuckCursorImg, cursorOffset, CursorMode.Auto);
            //Debug.Log("picked up");
        }

        else if (puckMovement.currentState == PuckState.PutDown)
        {
            Cursor.SetCursor(noPuckCursorImg, cursorOffset, CursorMode.Auto);
            //Debug.Log("place it");
        }
    }
}