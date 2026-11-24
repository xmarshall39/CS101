using UnityEngine;
using System.Collections.Generic;

public class StockSelect : MonoBehaviour
{
    public List<GameObject> stockList; // 5 elements
    public int currentStock = 3;
    public GameObject Stock;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void SelectStock(int optionIndex)
    {
        stockList[1] = ;
        if (optionIndex > stockList.Count - 1)
        {
            optionIndex = stockList.Count - 1;
        }
        if (optionIndex < 0)
        {
            optionIndex = 0;
        }
    }
}
