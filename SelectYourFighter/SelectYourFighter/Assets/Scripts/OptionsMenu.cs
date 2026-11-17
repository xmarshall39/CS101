using UnityEngine;
using TMPro;
using System.Collections.Generic;

public class OptionsMenu : MonoBehaviour
{
    public List<DifficultyOption> optionsList; // 5 elements
    public int currentOption = 1;
    public TextMeshProUGUI difficultyText;


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        SelectOption(currentOption);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void SelectOption(int optionIndex)
    {
        if (optionIndex > optionsList.Count - 1)
        {
            optionIndex = optionsList.Count - 1;
        }
        if (optionIndex < 0)
        {
            optionIndex = 0;
        }
        difficultyText.text = optionsList[optionIndex].difficultyText;
        difficultyText.color = optionsList[optionIndex].difficultyColor;
        currentOption = optionIndex;
    }
    public void IncreaseDifficulty()
    {
        SelectOption(currentOption + 1);
    }
    public void DecreaseDifficulty()
    {
        SelectOption(currentOption - 1);
    }
}

[System.Serializable]
public class DifficultyOption
{
    public string difficultyText;
    public Color difficultyColor;
}
/*
 * change difficulty text on arrow click and its color
 * arrows flashing
 * when arrow reaches last/first options, make arrow invisible/not clickable
 * change stock amounts from 1 - 5
 */