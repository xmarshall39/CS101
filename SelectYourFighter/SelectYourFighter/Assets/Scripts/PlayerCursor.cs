using UnityEngine;

public class PlayerCursor : MonoBehaviour
{
    [Header("Cursor Sprites")]
    public Sprite defaultCursorImg;
    public Sprite holdPuckCursorImg;
    public Sprite noPuckCursorImg;

    public PlayerPuckMovement puckMovement;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        Cursor.SetCursor(defaultCursorImg.texture, Vector2.zero, CursorMode.Auto);
    }

    // Update is called once per frame
    void Update()
    {
        if (puckMovement.currentState == PuckState.Hidden)
        {
            Cursor.SetCursor(defaultCursorImg.texture, Vector2.zero, CursorMode.Auto);
            //Debug.Log("hide it");
        }

        else if (puckMovement.currentState == PuckState.PickUp)
        {
            Cursor.SetCursor(holdPuckCursorImg.texture, Vector2.zero, CursorMode.Auto);
            //Debug.Log("picked up");
        }

        else if (puckMovement.currentState == PuckState.PutDown)
        {
            Cursor.SetCursor(noPuckCursorImg.texture, Vector2.zero, CursorMode.Auto);
            //Debug.Log("place it");
        }
    }
}