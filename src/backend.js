import axios from 'axios';

let $backend = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
  return response;
}, function (error) {
  // eslint-disable-next-line
  console.log(error);
  return Promise.reject(error);
})

$backend.$fetchLoans = async (axiosConfig) => {
  const response = await $backend.get(`loans/`, axiosConfig);
  return response.data;
}

$backend.$fetchPendingLoans = async (axiosConfig) => {
  const response = await $backend.get(`loans/list_pending/`, axiosConfig);
  return response.data;
}

$backend.$updateLoan = async (id, payload, axiosConfig) => {
  const response = await $backend.patch(`loans/${id}/`, payload, axiosConfig)
  return response;
}

$backend.$postLoan = async (payload, axiosConfig) => {
  const response = await $backend.post(`loans/`, payload, axiosConfig);
  return response;
}



export default $backend