using UnityEngine;

public class PlayerPuckMovement : MonoBehaviour
{
    public enum PuckState
    {
        PickUp,
        PutDown,
        ReturntoCursor,
        Hidden
    }

    public PuckState currentState = PuckState.Hidden;
    
    void SetPuckState(PuckState newState)
    {
        switch (currentState)
        {
            case PuckState.Hidden:
                break;

            case PuckState.PickUp:
                break;

            case PuckState.PutDown:
                break;

            case PuckState.ReturntoCursor:
                break;

            default:
                break;
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
