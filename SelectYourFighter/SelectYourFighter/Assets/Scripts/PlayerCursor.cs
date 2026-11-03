using UnityEngine;

public class PlayerCursor : MonoBehaviour
{
    [Header("Cursor Sprites")]
    public Sprite defaultCursorImg;



    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        Cursor.SetCursor(defaultCursorImg.texture, Vector2.zero, CursorMode.Auto);
    }

    // Update is called once per frame
    void Update()
    {

    }
}