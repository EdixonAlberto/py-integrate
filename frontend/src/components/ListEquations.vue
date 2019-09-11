<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de Ecuaciones</h2>

        <div class="col-md-12">
          <b-table striped hover :items="equations" :fields="fields"></b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ListEquations",
  data() {
    return {
      fields: [
        { key: "name", label: "Nombre" },
        { key: "equation", label: "Ecuanción" },
        { key: "action", label: "Acción" }
      ],
      equations: []
    };
  },

  methods: {
    getEquations() {
      const path = "localhost:8000/api/equations";

      axios.get(path).then(resp => {
          this.equations = resp.data;
        })
        .catch(er => {
          console.log(er);
        });
    },

    created() {
        this.getEquations();
    }
  }
};
</script>
