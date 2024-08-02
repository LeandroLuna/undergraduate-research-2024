
interface Prediction {
    id: number,
    fractured: boolean,
    img_file_path: string,
    img_labels_file_path: string,
    object?: string[] 
}

interface Predictions {
    results: {
        id: number,
        img_url: string,
        detect?: Prediction,
        segment?: Prediction
    }[];
}

export { Predictions, Prediction };