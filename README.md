tailwind.config.js 에서 사용자 정의 값 만들기

class 확장하는 방법

module.exports = {
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",  이 세개중에서 오른쪽 값들은 css를 위한 값들이고, 오른쪽에 있는 값들은 classname을 위한 값들이다. 이처럼 필요한 클래스가 없을때 만들어 사용할 수 있음.
        그러니까 theme를 확장해주는 방식으로 클래스를 커스터마이징할 수 있음.

        theme에서 tailwind의 디폴드 값을 바꿀수도 있고 extend로 확장해서 사용할 수 있다.

        "50vh": "50vh",
        "75vh": "75vh"
      },
      borderRadius: {
        xl: "1.5rem"
      }
    }
  },
  variants: {},
  plugins: []
};




