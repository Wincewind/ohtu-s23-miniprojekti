import React, { useState } from 'react'
import Dropdown from './Dropdown'
import BookForm from './BookForm'
import ArticleForm from './ArticleForm'

const FormContainer = (props) => {
    const { formData, onInputChange, handleSubmit } = props
    const [referenceType, setReferenceType] = useState('Book')

    const handleDropdownChange = (selectedValue) => {
        setReferenceType(selectedValue)
    }

    return (
        <>
            <Dropdown
                selectedValue={referenceType}
                onDropdownChange={handleDropdownChange}
            />
            <br />
            <br />
            {referenceType === 'Book' && (
                <BookForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={handleSubmit}
                />
            )}
            {referenceType === 'Article' && (
                <ArticleForm
                    formData={formData}
                    onInputChange={onInputChange}
                    handleSubmit={handleSubmit}
                />
            )}
        </>
    )
}

export default FormContainer
