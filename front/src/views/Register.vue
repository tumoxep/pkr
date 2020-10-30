<template>
  <div class="register-view">
    <h1>Регистрация</h1>
    <input type="text" placeholder="Имя пользователя" v-model="username" />
    <input type="email" placeholder="Email" v-model="email" />
    <input type="password" placeholder="Пароль" v-model="password1" />
    <input
      type="password"
      placeholder="Подтверждение пароля"
      v-model="password2"
    />
    <button @click="register">Зарегистрироваться</button>
  </div>
</template>

<script>
import { ENDPOINTS } from "@/constants";
import { postData } from "@/utils";

export default {
  name: "RegisterView",
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    async register() {
      postData(ENDPOINTS.REGISTER, {
        username: this.username,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
      });
    },
  },
};
</script>
