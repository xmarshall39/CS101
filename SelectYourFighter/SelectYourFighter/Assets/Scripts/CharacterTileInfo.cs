using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEngine.EventSystems;
public class CharacterTileInfo : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
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



    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {

    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        PlayerPuckMovement puck = FindAnyObjectByType<PlayerPuckMovement>();
        puck.SetPuckState((int)PuckState.PickUp);

    }

    public void OnPointerExit(PointerEventData eventData)
    {
        PlayerPuckMovement puck = FindAnyObjectByType<PlayerPuckMovement>();
        puck.SetPuckState((int)PuckState.Hidden);
    }
}
