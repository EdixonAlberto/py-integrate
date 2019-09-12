<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de Ecuaciones</h2>
        <div class="col-md-12">
          <div class="text-right">
            <b-button size="sm" variant="success">Agrega</b-button>
          </div>
          <b-table
            striped
            hover
            :items="equations"
            :fields="fields"
            :head-variant="'dark'"
            :busy="loaded"
          >
            <template v-slot:table-busy>
              <div class="text-center text-dark my-2">
                <b-spinner class="align-middle"></b-spinner>
                <strong>Cargando...</strong>
              </div>
            </template>
            <template v-slot:cell(action)="row">
              <b-button size="sm" variant="outline-primary">Editar</b-button>
              <b-button size="sm" variant="outline-danger">Eliminar</b-button>
            </template>
          </b-table>
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
      loaded: true,

      fields: [
        { key: "name", label: "Nombre" },
        { key: "equation", label: "Ecuanción" },
        { key: "action", label: "" }
      ],
      // equations: []
      equations: [
        {
          name: "suma",
          equation: "x + y"
        },
        {
          name: "resta",
          equation: "x - y"
        },
        {
          name: "polinomio",
          equation: "2x^2"
        }
      ]
    };
  },

  methods: {
    getEquations() {
      const path = "http://localhost:8000/api/equations/";

      axios
        .get(path)
        .then(resp => {
          this.equations = resp.data;
        })
        .catch(er => {
          console.log(er);
        });
    }
  },

  created() {
    // this.getEquations();
    setTimeout(() => {
      this.loaded = false;
    }, 2000);
  }
};
</script>
