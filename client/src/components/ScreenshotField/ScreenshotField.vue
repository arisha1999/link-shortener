<template> 
    <div> 
        <img :src="screenshotUrl" alt="Screenshot"> 
    </div> 
</template> 

<script> 
    export default { 
        props: { 
            screenshotUrl: { 
                type: String, 
                default: '' 
            } 
        } 
    } 
</script>