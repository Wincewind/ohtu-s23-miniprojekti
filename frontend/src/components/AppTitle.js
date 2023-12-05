import Typography from '@mui/material/Typography'

const AppTitle = ({ titleText }) => (
    <Typography
        sx={{ flex: '1 1 100%' }}
        variant="h4"
        id="appTitle"
        component="div"
    >
        {titleText}
    </Typography>
)

export default AppTitle
