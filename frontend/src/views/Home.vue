<template>
  <div class="container-fluid">
    <div class="profile">
      <div class="row">
        <div class="col-2 h-50">
          <h4>@username</h4>
        </div>
      </div>
      <div class="row">
        <div class="col-2 h-50">
          <h4>@email</h4>
        </div>
      </div>
      <div class="row justify-content-md-center">
        <div class="col text-center" style="margin:20px">
          <p>Portfolio Name : </p>
        </div>
      </div>
      <div class="info">

      </div>
    </div>
    <div class="table">
      <table class="table table-light">
        <thead>
        <tr>
          <th scope="col">№</th>
          <th scope="col">Name</th>
          <th scope="col">Count</th>
          <th scope="col">Total Cost</th>
          <th scope="col">Current Price</th>
          <th scope="col">% up/down</th>
          <th scope="col">Graph</th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
          <td>@mdo</td>
          <td>@mdo</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
          <td>@fat</td>
          <td>@fat</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Larry</td>
          <td>the Bird</td>
          <td>@twitter</td>
          <td>@twitter</td>
          <td>@twitter</td>
          <td>@twitter</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      portfolio: '',
      coins: [],

    }
  }
}
</script>
