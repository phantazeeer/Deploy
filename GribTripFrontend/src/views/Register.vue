<script setup>
import { FormKit } from '@formkit/vue'
// This is just a mock of an actual axios instance.s
const axios = {
  post: () => new Promise((r) => setTimeout(r, 2000)),
}

async function login(credentials) {
  const res = await axios.post(credentials)
  // do some login things now
  alert('Logged in!')
}
</script>
<template>
  <div class="grid grid-cols-2 fixed">
    <div class="grid"><img src="/public/image.png" /></div>
    <div class="grid m-20">
      <h2 class="">Регистрация</h2>
      <FormKit type="form" submit-label="Login" @submit="login">
        <FormKit name="email" label="Email address" validation="required|email" />
        <FormKit type="password" name="password" label="Password" validation="required" />
      </FormKit>
      <div v-if="submitted">
        <h2 class="text-xl text-green-500">Submission successful!</h2>
      </div>
    </div>
  </div>
</template>
<style scoped>
h1 {
  font-size: calc(24px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h2 {
  font-size: calc(12px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h3 {
  font-size: calc(8px + (16 + 16 * 0.7) * ((110vw - 320px) / 1280));
}
h4 {
  font-size: calc((5 + 4 * 0.7) * ((110vw - 320px) / 1280) + 2px);
  align-content: center;
}
h5 {
  font-size: calc((6 + 4 * 0.7) * ((110vw - 320px) / 1280) + 3px);
  align-content: center;
}
p {
  font-size: calc((10 + 4 * 0.7) * ((110vw - 320px) / 1280) + 5px);
  align-content: center;
}
h6 {
  font-size: calc((14 + 4 * 0.7) * ((110vw - 320px) / 1280) + 6px);
  align-content: center;
}
</style>
