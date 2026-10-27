using UnityEngine;
using System.Collections.Generic;
using TMPro;


public class CharacterSelectManager : MonoBehaviour
{
    [HideInInspector]
    public CharacterTileInfo selectedCharacter = null;

    enum Difficulty
    {
        VeryEasy,
        Easy,
        Normal,
        Hard,
        VeryHard
    }

    public List<Color> difficultyColors;

    public int stockAmount;

    public Animator readyOverlay;

    public int totalHighScore;
    public TextMeshProUGUI highScoreText;
    public TextMeshProUGUI totalHighScoreText;
    public TextMeshProUGUI charText;

    void SelectCharacter(CharacterTileInfo character)
    {
        if (!selectedCharacter)
        {
            // open doors
            
        }

        else
        {
            /*
              then selectedCharacter = character
                place the playerPuck
                change cursor icons
                play readyOverlay
                flashCharacterTile
                Spin Character
                play Character Name Audio
                change:
                    scores
                    names
                    levels (PlasticGui known level by default)
                    stock amount (PlasticGui known stock by default)
            */
            highScoreText.text = character.highScore.ToString();
            charText.text = character.charName;
        }

    }
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
