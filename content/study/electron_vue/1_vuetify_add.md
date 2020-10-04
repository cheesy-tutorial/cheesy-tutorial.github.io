---
title: "1. Electron Vue Vuetify 추가하기"
metaTitle: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 모음집"
metaDescription: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 정리 되어 있음"
---


# Vuetify 추가하기
* * *
Vuetify를 Electron에 적용하는 방법에 대해 알아봅니다.

### 1. vuetify 모듈 설치 후, 적용
1-1. 설치 명령어
``` bash
## npm
yarn add vuetify
```
![ex_screenshot](./assets//yarn-add-vuetify.png)

2-1. 모듈 적용 방법
프로젝트의 src/render/index.js에 vuetify 모듈을 import 해주면 사용가능하다. 아래와 같이 추가해주자 ^^

- src/render/index.js
  ``` javascript
  import App from './App'
  import router from './router'
  import store from './store'
  /// 아래 추가 //////////////////////
  import Vuetify from 'vuetify'
  import 'vuetify/dist/vuetify.min.css'

  Vue.use(Vuetify)
  /////////////////////////////////
  if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
  Vue.http = Vue.prototype.$http = axios
  Vue.config.productionTip = false
  ```
  이제 적용이 끝났다~! vuetify 컴포넌트를 직접 사용해보자

### 2. vuetify 컴포넌트 사용하기
2-1. 소스 수정
vuetify 컴포넌트 중의 하나인 버튼을 테스트해보려고 합니다. 그래서 src/render/compomnents/SystemInformaion.vue 파일을 열어서 모두 내용을 지우고 아래 내용을 추가해주세요
``` javascript
<template>
  <v-row align="center">
    <v-col class="text-center" cols="12" sm="4">
      <div class="my-2">
        <v-btn depressed small>Normal</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed small color="primary">Primary</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed small color="error">Error</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed small disabled>Disabled</v-btn>
      </div>
    </v-col>

    <v-col class="text-center" cols="12" sm="4">
      <div class="my-2">
        <v-btn depressed>Normal</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed color="primary">Primary</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed color="error">Error</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed disabled>Disabled</v-btn>
      </div>
    </v-col>

    <v-col class="text-center" cols="12" sm="4">
      <div class="my-2">
        <v-btn depressed large>Normal</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed large color="primary">Primary</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed large color="error">Error</v-btn>
      </div>
      <div class="my-2">
        <v-btn depressed large disabled>Disabled</v-btn>
      </div>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        electron: process.versions.electron,
        name: this.$route.name,
        node: process.versions.node,
        path: this.$route.path,
        platform: require('os').platform(),
        vue: require('vue/package.json').version
      }
    }
  }
</script>

<style scoped>
  .title {
    color: #888;
    font-size: 18px;
    font-weight: initial;
    letter-spacing: .25px;
    margin-top: 10px;
  }

  .items { margin-top: 8px; }

  .item {
    display: flex;
    margin-bottom: 6px;
  }

  .item .name {
    color: #6a6a6a;
    margin-right: 6px;
  }

  .item .value {
    color: #35495e;
    font-weight: bold;
  }
</style>
```

2-2. 실행
결과를 확인해보기 위해 프로젝트를 실행해보겠습니다.
``` bash
yarn run dev
```
2-3. 실행 결과
![ex_screenshot](./assets//new-project-vuetify-test.png)