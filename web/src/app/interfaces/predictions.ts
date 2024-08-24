
interface PredictionModel {
    id: number,
    fractured: boolean,
    img_file_path: string,
    img_labels_file_path: string,
    object?: string[] 
}

interface Prediction { 
    results: PredictionModel
}

interface Predictions {
    id: number,
    img_url: string,
    detect?: PredictionModel,
    segment?: PredictionModel
}

interface PredictionsList {
    results: {
        id: number,
        img_url: string,
        detect?: PredictionModel,
        segment?: PredictionModel
    }[];
}

export { Predictions, Prediction, PredictionsList, PredictionModel };