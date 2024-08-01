
interface Prediction {
    id: int,
    fractured: boolean,
    img_file_path: string,
    img_labels_file_path: string,
    object?: string[] 
}

interface Predictions {
    results: {
        id: int,
        img_url: string,
        detect?: Prediction[],
        segment?: Prediction[]
    }
}

export default Predictions, Prediction;