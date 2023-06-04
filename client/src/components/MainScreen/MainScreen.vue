<template>
    <div class="main-container">
        <GenerateButton /> 
        <ScreenshotField :screenshotUrl="screenshotUrl" /> 
        <ErrorAlert :errorMessage="errorMessage" />
    </div>
</template>

<script>
    import GenerateButton from '@/components/GenerateButton/GenerateButton.vue' 
    import ErrorAlert from '@/components/ErrorAlert/ErrorAlert.vue' 
    export default { 
        components: { 
            GenerateButton,
            ErrorAlert 
        }, 
        data() { 
            return { 
                fullUrl: '', 
                shortUrl: '', 
                screenshotUrl: '', 
                errorMessage: '' 
            } 
        }, 
    }
</script>

<style>
    .main-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 30px;
    }
</style>


