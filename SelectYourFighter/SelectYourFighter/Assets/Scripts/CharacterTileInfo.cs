using UnityEngine;
using TMPro;
public class CharacterTileInfo : MonoBehaviour
{
    [Header("Character Tile Sprites")]
    public bool isLocked;
    public Sprite lockedSprite;
    public Sprite unlockedSprite;

    [Header("Character Name")]
    public string charName;
    public AudioClip charAnnounced;

    [Header("Character Options")]
    public GameObject charModel;
    public int highScore;
    public Animator selectFlash;
    public Sprite stockIcon;

    bool isSelected;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
