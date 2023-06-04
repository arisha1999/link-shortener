<template>
    <div class="main-container">
        <GenerateLink /> 
        <ScreenshotField :screenshotUrl="screenshotUrl" /> 
        <ErrorAlert :errorMessage="errorMessage" />
    </div>
</template>

<script>
    import GenerateLink from '@/components/GenerateLink/GenerateLink.vue' 
    import ErrorAlert from '@/components/ErrorAlert/ErrorAlert.vue' 
    export default { 
        components: { 
            GenerateLink,
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


