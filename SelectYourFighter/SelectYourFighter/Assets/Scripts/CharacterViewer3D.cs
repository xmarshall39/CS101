using UnityEngine;

public class CharacterViewer3D : MonoBehaviour
{
    public GameObject charStage;
    public int frameRate;
    public float rotationSpeed = 1;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        float rotateRate = rotationSpeed * Time.deltaTime;
        charStage.transform.Rotate(new Vector3(0, rotateRate, 0), Space.World);
        Application.targetFrameRate = frameRate;
    }
}
