import * as React from 'react'
import PropTypes from 'prop-types'
import { alpha } from '@mui/material/styles'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import IconButton from '@mui/material/IconButton'
import Tooltip from '@mui/material/Tooltip'
import DeleteIcon from '@mui/icons-material/Delete'
import DownloadIcon from '@mui/icons-material/Download'
import { deleteReferencesInArray } from '../../api/referenceService'
import { convertToBibTex } from '../../util/bibTexUtil'

const ReferenceTableToolbar = (props) => {
    const { numSelected, selected, onDelete: fetchReferences, rows } = props

    const handleDelete = async () => {
        try {
            await deleteReferencesInArray(selected)
            await fetchReferences()
        } catch (error) {
            console.error('Error fetching data: ', error)
        }
    }

    const handleDownload = async () => {
        const selectedRows = rows.filter((row) =>
            selected.includes(row.book_id)
        )

        const bibTexString = convertToBibTex(selectedRows)
        const fileToDownload = new Blob([bibTexString], { type: 'text/plain' })

        const downloadLink = document.createElement('a')
        downloadLink.href = URL.createObjectURL(fileToDownload)
        downloadLink.download = 'exportedReferences.bib'

        document.body.appendChild(downloadLink)
        downloadLink.click()
        document.body.removeChild(downloadLink)
    }

    return (
        <Toolbar
            sx={{
                pl: { sm: 2 },
                pr: { xs: 1, sm: 1 },
                ...(numSelected > 0 && {
                    bgcolor: (theme) =>
                        alpha(
                            theme.palette.primary.main,
                            theme.palette.action.activatedOpacity
                        ),
                }),
            }}
        >
            {numSelected > 0 ? (
                <Typography
                    sx={{ flex: '1 1 100%' }}
                    color="inherit"
                    variant="subtitle1"
                    component="div"
                >
                    {numSelected} selected
                </Typography>
            ) : (
                <Typography
                    sx={{ flex: '1 1 100%' }}
                    variant="h6"
                    id="tableTitle"
                    component="div"
                >
                    All references
                </Typography>
            )}

            {numSelected > 0 && (
                <>
                    <Tooltip title="Download">
                        <IconButton onClick={handleDownload}>
                            <DownloadIcon />
                        </IconButton>
                    </Tooltip>
                    <Tooltip title="Delete">
                        <IconButton onClick={handleDelete}>
                            <DeleteIcon />
                        </IconButton>
                    </Tooltip>
                </>
            )}
        </Toolbar>
    )
}

ReferenceTableToolbar.propTypes = {
    numSelected: PropTypes.number.isRequired,
    selected: PropTypes.array.isRequired,
    onDelete: PropTypes.func.isRequired,
}

export default ReferenceTableToolbar
