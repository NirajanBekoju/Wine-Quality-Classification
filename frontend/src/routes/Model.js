import React, { useState } from 'react'
import axios from 'axios'

const Model = () => {
    const [formData, setFormData] = useState({
        fixed_acidity: "",
        volatile_acidity: "",
        citric_acid: "",
        residual_sugar: "",
        chlorides: "",
        free_sulfur_dioxide: "",
        total_sulfur_dioxide: "",
        density: "",
        pH: "",
        sulphates: "",
        alcohol: ""
    })

    const [predictionData, setPredictionData] = useState({})

    const handleChange = (e) => {
        setFormData((prevFormData) => {
            return { ...prevFormData, [e.target.name]: e.target.value }
        })
    }

    const { fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol } = formData;

    const handleSubmit = (e) => {
        e.preventDefault();
        axios
            .post("model/predict/", {
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            })
            .then((res) => {
                console.log("From response")
                console.log(res.data)
                setPredictionData(res.data)
            })
            .catch((err) => {
                console.log("error occured")
            })
    }

    const showProgressBar = (value) => {
        value = value * 100
        if (isNaN(value)) {
            value = 0;
        }
        let widthValue = value.toString() + "%"

        const widthStyle = { "width": widthValue }

        return (
            <div className="progress mt-2" style={{ "height": "3px" }}>
                <div className="progress-bar bg-info" role="progressbar" style={widthStyle} aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
        )
    }

    const showPrediction = (data) => {
        return (
            <div>
                {data.map((value, index) => (
                    <div className='row'>
                        <div key={index} className='col-md-10  pb-3'>
                            {showProgressBar(value)}
                            {index}
                        </div>
                        <div className='col-md-2'>
                            {value.toFixed(2)}
                        </div>
                    </div>
                ))}
            </div>
        )
    }

    return (
        <div className='container'>
            <div className='row pt-4'>
                <div className='col-12'>
                    <h1>Wine Quality Prediction</h1>
                    {"error" in predictionData ?
                        <div className="alert alert-danger" role="alert">
                            Make sure all values are numbers.
                        </div>
                        : " "
                    }

                    <form onSubmit={(e) => handleSubmit(e)}>
                        <div className='row'>
                            <div className='col-md-2'>
                                <label htmlFor='fixed_acidity'>Fixed Acidity</label>
                                <input type='number' className='form-control' placeholder='fixed_acidity' name='fixed_acidity' value={fixed_acidity} onChange={(e) => handleChange(e)} autoFocus />
                            </div>

                            <div className='col-md-2'>
                                <label htmlFor='volatile_acidity'>Volatile Acidity</label>
                                <input type='number' className='form-control' placeholder='volatile_acidity' name='volatile_acidity' value={volatile_acidity} onChange={(e) => handleChange(e)} />
                            </div>

                            <div className='col-md-2'>
                                <label htmlFor=''>Citric Acid</label>
                                <input type='number' className='form-control' placeholder='citric_acid' name='citric_acid' value={citric_acid} onChange={(e) => handleChange(e)} />
                            </div>

                            <div className='col-md-2'>
                                <label htmlFor='residual_sugar'>Residual Sugar</label>
                                <input type='number' className='form-control' placeholder='residual_sugar' name='residual_sugar' value={residual_sugar} onChange={(e) => handleChange(e)} />
                            </div>
                            <div className='col-md-2'>
                                <label htmlFor='chlorides'>Chlorides</label>
                                <input type='number' className='form-control' placeholder='chlorides' name='chlorides' value={chlorides} onChange={(e) => handleChange(e)} />
                            </div>

                            <div className='col-md-2'>
                                <label htmlFor='free_sulfur_dioxide'>Free Sulfur Dioxide</label>
                                <input type='number' className='form-control' placeholder='free_sulfur_dioxide' name='free_sulfur_dioxide' value={free_sulfur_dioxide} onChange={(e) => handleChange(e)} />
                            </div>
                        </div>

                        <div className='row pt-4'>
                            
                            <div className='col-md-2'>
                                <label htmlFor='total_sulfur_dioxide'>Total Sulfur Dioxide</label>
                                <input type='number' className='form-control' placeholder='total_sulfur_dioxide' name='total_sulfur_dioxide' value={total_sulfur_dioxide} onChange={(e) => handleChange(e)} />
                            </div>
                            <div className='col-md-2'>
                                <label htmlFor='density'>Density</label>
                                <input type='number' className='form-control' placeholder='density' name='density' value={density} onChange={(e) => handleChange(e)} />
                            </div>
                
                            <div className='col-md-2'>
                                <label htmlFor='pH'>pH</label>
                                <input type='number' className='form-control' placeholder='pH' name='pH' value={pH} onChange={(e) => handleChange(e)} />

                            </div>
                            <div className='col-md-2'>
                                <label htmlFor='sulphates'>Sulphates</label>
                                <input type='number' className='form-control' placeholder='sulphates' name='sulphates' value={sulphates} onChange={(e) => handleChange(e)} />
                            </div>
                            <div className='col-md-2'>
                                <label htmlFor='alcohol'>Alcohol</label>
                                <input type='number' className='form-control' placeholder='alcohol' name='alcohol' value={alcohol} onChange={(e) => handleChange(e)} /></div>
                        </div>
                        <br />
                        <button type="submit" className="form-control btn btn-success">
                            Predict
                        </button>
                    </form>
                </div>
            </div>
            <div className='row'>
                <div className='col-md-6'>
                    {"lr2_pred" in predictionData ?
                        <div className='mt-4'>
                            Logistic Regression
                            {showPrediction(predictionData["lr2_pred"])}
                        </div> : ""}
                </div>
                <div className='col-md-6'>
                    {"xgb_pred" in predictionData ?
                        <div className='mt-4'>
                            XGBClassifier
                            {showPrediction(predictionData["xgb_pred"])}
                        </div> : ""}
                </div>
            </div>
        </div>
    )
}

export default Model