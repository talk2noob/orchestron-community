<template>
  <div>
    <b-container fluid>
      <loading :active.sync="reloadPage" :can-cancel="true"></loading>
      <common-table :pageCount="engagementsCount" :dataItems="engagementList" :headerTitle="headerTitles"
                    @createModal="createEngagement"
                    @updateModal="updateEngagement($event)"
                    @deleteModal="deleteEngagement($event)"
                    @clickPagination="clickPagination($event)"
      ></common-table>

      <!--create-->
      <b-modal
        ref="createEngagementModal"
        title="Create Engagement"
        size="lg"
        centered>
        <div>
          <form @submit.prevent="submitCreateEngagement">
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Name: *</label></b-col>
              <b-col sm="10">
                <b-form-input
                  v-model="engagementName"
                  type="text"
                  maxlength="255"
                  class="inline-form-control"
                  placeholder="Enter Engagement Name" :state="!$v.engagementName.$invalid"></b-form-input>
                  <label id="input_count">
                    {{ error_msgs['eng_name_count'] }}
                  </label>
                <p v-if="error_msgs['name']" style="text-align: left;position: fixed;" class="error"> * {{ error_msgs['name_msg'] }}</p>
              </b-col>
            </b-row>
            <!--   <b-col sm="12">
                  <br>
                  <p  v-if="error_msgs['name']" style="text-align: left;" class="error"> * {{ error_msgs['name_msg'] }}</p>
              </b-col> -->
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Description: *</label></b-col>
              <b-col sm="10">
                <b-form-textarea
                  v-model="engagementDesc"
                  placeholder="Enter Description"
                  :rows="3"
                  :max-rows="6">
                  <p v-if="error_msgs['desc']" style="text-align: left;" class="error"> * {{ error_msgs['desc_msg']
                    }}</p>
                </b-form-textarea>
              </b-col>
            </b-row>
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Application: *</label></b-col>
              <b-col sm="10">
                <v-select
                  :options="applicationOption"
                  placeholder="Select Application"
                  v-model="application"
                  :state="!$v.application.$invalid"></v-select>
                <p v-if="error_msgs['app']" style="text-align: left;" class="error"> * {{ error_msgs['app_msg'] }}</p>
              </b-col>
            </b-row>
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Date: *</label></b-col>
              <b-col sm="10">
                <date-picker
                  v-model="engagementDateRange"
                  range :shortcuts="shortcuts"
                  format="yyyy-MM-dd"
                  lang="en" width="100%"
                  :not-before="today" :state="!$v.engagementDateRange.$invalid"></date-picker>
                <p v-if="error_msgs['date']" style="text-align: left;" class="error"> * {{ error_msgs['date_msg'] }}</p>
              </b-col>
              <!--  <b-col sm="12">
                 <br>
                  <p  v-if="error_msgs['date']" style="text-align: left;" class="error"> * {{ error_msgs['date_msg'] }}</p>
               </b-col> -->
            </b-row>
            <br>
          </form>
        </div>
        <b-col cols="12" slot="modal-footer">
          <div class="pull-right" style="float: right">
            <button type="button" class="btn btn-orange-close pull-right" @click=" closeCreateEngagement() "> Close
            </button>
            <button type="button"
                    class="btn btn-orange-submit pull-right"
                    data-dismiss="modal"
                    @click=" submitCreateEngagement() "
                    v-if="!$v.engagementName.$invalid && !$v.engagementDesc.$invalid && !$v.application.$invalid && !$v.engagementDateRange.$invalid">
              Submit
            </button>
          </div>
        </b-col>
      </b-modal>

      <!--update-->
      <b-modal
        ref="updateEngagementModal"
        title="Update Engagement"
        size="lg"
        centered>
        <div>
          <form @submit.prevent="submitUpdateEngagement">
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Name: *</label></b-col>
              <b-col sm="10">
                <b-form-input
                  v-model="updateEngagementName"
                  type="text"
                  maxlength="255"
                  class="inline-form-control"
                  placeholder="Enter Engagement Name" :state="!$v.updateEngagementName.$invalid"></b-form-input>
                  <label id="input_count">
                    {{ error_msgs['eng_upd_name_count'] }}
                  </label>
                <p v-if="error_msgs['name']" style="text-align: left;position: fixed;" class="error"> * {{ error_msgs['name_msg'] }}</p>
                <!--<p v-if="!$v.projectName.required">The name field is required!</p>-->
                <!--<p v-if="!$v.projectName.minLength">The name field is minimum 3!</p>-->
              </b-col>

              <!--  <b-col sm="12">
                 <br>
                 <p  v-if="error_msgs['name']" style="text-align: left;" class="error"> * {{ error_msgs['name_msg'] }}</p>
               </b-col> -->
            </b-row>
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Description: *</label></b-col>
              <b-col sm="10">
                <b-form-textarea
                  v-model="updateEngagementDesc"
                  placeholder="Enter Description"
                  :rows="3"
                  :max-rows="6" :state="!$v.updateEngagementDesc.$invalid">
                </b-form-textarea>
                <p v-if="error_msgs['desc']" style="text-align: left;" class="error"> * {{ error_msgs['desc_msg'] }}</p>
              </b-col>
            </b-row>
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Application: *</label></b-col>
              <b-col sm="10">
                <v-select
                  :options="applicationOption"
                  v-model="updateApplication"
                  :state="!$v.updateApplication.$invalid"></v-select>
                <p v-if="error_msgs['app']" style="text-align: left;" class="error"> * {{ error_msgs['app_msg'] }}</p>
              </b-col>
            </b-row>
            <br>
            <b-row class="my-1">
              <b-col sm="2"><label class="label">Date: *</label></b-col>
              <b-col sm="10">
                <date-picker
                  v-model="updateEngagementDateRange"
                  range :shortcuts="shortcuts"
                  format="yyyy-MM-dd"
                  lang="en" width="100%"
                  :not-before="today" :state="!$v.updateEngagementDateRange.$invalid"></date-picker>
                <p v-if="error_msgs['date']" style="text-align: left;" class="error"> * {{ error_msgs['date_msg'] }}</p>
              </b-col>
              <!--   <b-col sm="12">
                  <br>
                   <p  v-if="error_msgs['date']" style="text-align: left;" class="error"> * {{ error_msgs['date_msg'] }}</p>
                </b-col> -->
            </b-row>
            <br>
          </form>
        </div>
        <b-col cols="12" slot="modal-footer">
          <div class="pull-right" style="float: right">
            <button type="button" class="btn btn-orange-close pull-right" @click=" closeUpdateEngagement() "> Close
            </button>
            <button type="button"
                    class="btn btn-orange-submit pull-right"
                    data-dismiss="modal"
                    @click=" submitUpdateEngagement() "
                    v-if="!$v.updateEngagementName.$invalid && !$v.updateEngagementDesc.$invalid && !$v.updateApplication.$invalid && !$v.updateEngagementDateRange.$invalid">
              Submit
            </button>
          </div>
        </b-col>
      </b-modal>

      <!--delete-->
      <b-modal ref="deleteEngagementModal" title="Delete Engagement" centered size="lg">
        <div>
          <form @submit.prevent="submitDeleteEngagement">
            <p class="delete-header">Are you sure want to delete this engagement ?</p>
            <br>
          </form>
        </div>
        <b-col cols="12" slot="modal-footer">
          <div class="pull-right" style="float: right;">
            <button type="button" class="btn btn-orange-close" @click=" closeDeleteEngagement() ">Cancel</button>
            <button type="button" class="btn btn-orange-submit"
                    data-dismiss="modal" @click=" submitDeleteEngagement() ">
              Delete
            </button>
          </div>
        </b-col>
      </b-modal>
      <!-- {{engagementPagnatedList}} -->
    </b-container>
  </div>
</template>

<script>
  import CommonTable from '../../components/Projects/CommonTable'
  import axios from '@/utils/auth'
  import {required, minLength} from 'vuelidate/lib/validators'
  import DatePicker from 'vue2-datepicker'
  import Loading from 'vue-loading-overlay'
  import 'vue-loading-overlay/dist/vue-loading.min.css'
  import {notValidUser} from '@/utils/checkAuthUser'

  export default {
    name: 'Engagements',
    components: {
      CommonTable,
      DatePicker,
      Loading
    },
    data() {
      return {
        isLoading: false,
        engagementList: [],
        headerTitles: 'List of Engagements',
        individualEngagementUrl: '',
        applicationOption: [],
        engagementPagnatedList: [],
        engagementName: '',
        engagementDesc: '',
        application: '',
        engagementDateRange: '',
        updateEngagementName: '',
        updateEngagementDesc: '',
        updateApplication: '',
        updateEngagementDateRange: '',
        engagementId: '',
        engagementsCount: 0,
        isPaginated: false,
        reloadPage: false,
        today: new Date(),
        error_msgs: {"name": false, "date": false, "name_msg": "", "date_msg": "","eng_name_count":255, "eng_upd_name_count":255},
        shortcuts: [
          {
            // text: 'Today',
            start: new Date(),
            end: new Date()
          }
        ]
      }
    },
    validations: {
      engagementName: {
        required,
        minLength: minLength(1)
      },
      engagementDesc: {
        required,
        minLength: minLength(3)
      },
      application: {
        required
      },
      engagementDateRange: {
        required
      },
      updateEngagementName: {
        required,
        minLength: minLength(1)
      },
      updateEngagementDesc: {
        required,
        minLength: minLength(3)
      },
      updateApplication: {
        required
      },
      updateEngagementDateRange: {
        required
      }
    },
    created() {
      this.org = localStorage.getItem('org')
      this.token = localStorage.getItem('token')
      this.fetchData()
    },
    watch: {
      'engagementName': function (value_name) {
        this.error_msgs['eng_name_count'] = 255-value_name.length
        if (value_name.length > 254) {
          this.error_msgs['name'] = true
          this.error_msgs['name_msg'] = 'Max Length is 255 Characters'
        } else {
          this.error_msgs['name'] = false
        }
      },
      'updateEngagementName': function (value_name) {
         this.error_msgs['eng_upd_name_count'] = 255-value_name.length

        if (value_name.length > 254) {
          this.error_msgs['name'] = true
          this.error_msgs['name_msg'] = 'Max Length is 255 Characters'
        } else {
          this.error_msgs['name'] = false
        }
      },
      'application': function (value_name) {
        this.error_msgs['app'] = false
      },
      'updateApplication': function (value_name) {
        this.error_msgs['app'] = false
      },
      'updateEngagementDateRange': function (value_name) {
        this.error_msgs['date'] = false
      },

      'engagementDateRange': function (value_name) {
        this.error_msgs['date'] = false
      },
      'updateEngagementDesc': function (value_name) {
        this.error_msgs['date'] = false
      },
      'engagementDesc': function (value_name) {
        this.error_msgs['date'] = false
      }
    },
    updated() {
      if (this.isLoading) {
        this.$nextTick(() => {
          this.applicationOption = []
          this.engagementList = []
          // this.engagementPagnatedList = []
          this.fetchData()
        })
        this.isLoading = false
      }
      if (this.isPaginated) {
        // this.fetchData()

        this.$nextTick(() => {
          this.engagementList = this.engagementPagnatedList
          
        })
        this.isPaginated = false
      }
    },
    methods: {
      fetchData() {
        if (this.org && this.token) {
          this.reloadPage = true
          this.engagementList = []
          axios.get('/engagements/')
            .then(res => {
              this.engagementList = []
              this.engagementsCount = res.data.count
              for (const value of res.data.results) {

                this.engagementList.push({
                  name: {vul_name: value.name},
                  sev: value.severity,
                  id: value.id,
                  url: 'individual_engagement/' + value.id + '/',
                  appName: value.app_details.name,
                  engId: false
                })
              }
            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
              notValidUser()
              this.$router.push('/')
            }
            this.reloadPage = false

            if (error.res.status === 404) {
              this.$router.push('/not_found')
            } else if (error.res.status === 404) {
              this.$router.push('/forbidden')
            } else {
              this.$router.push('/error')
            }
          })

          axios.get('/applications/list/')
            .then(res => {
              this.applicationOption = []
              for (const value of res.data) {
                this.applicationOption.push({value: value.id, label: value.name})
              }
              this.reloadPage = false
            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
              notValidUser()
              this.$router.push('/')
            }
            this.reloadPage = false
            if (error.response.status === 404) {
              this.$router.push('/not_found')
            } else if (error.response.status === 404) {
              this.$router.push('/forbidden')
            } else {
              this.$router.push('/error')
            }
          })

        } else {
          notValidUser()
          this.$router.push('/')
        }
      },
      clickPagination(event) {
        if (this.org && this.token) {
          if (event.page) {
            if (event.page > 1) {
              this.reloadPage = true

              axios.get('/engagements/?page=' + event.page)
                .then(res => {
                  this.engagementPagnatedList = []
                  this.engagementList = []
                  for (const value of res.data.results) {
                    this.engagementPagnatedList.push({
                      name: {vul_name: value.name},
                      sev: value.severity,
                      id: value.id,
                      url: 'individual_engagement/' + value.id + '/',
                      appName: value.app_details.name,
                      engId: value.uniq_id
                    })
                  }
                  this.engagementList = this.engagementPagnatedList
                  this.reloadPage = false

                }).catch(error => {
                if (error.response.data.detail === 'Signature has expired.'){
                  notValidUser()
                  this.$router.push('/')
                }
                this.reloadPage = false

                if (error.response.status === 404) {
                  this.$router.push('/not_found')
                } else if (error.response.status === 404) {
                  this.$router.push('/forbidden')
                } else {
                  this.$router.push('/error')
                }
              })
              this.isPaginated = true
              this.reloadPage = false

            } else {
              this.fetchData()
            }
          } else {
            this.fetchData()
          }
        } else {
          notValidUser()
          this.$router.push('/')
        }
      },
      createEngagement() {
        this.error_msgs = {"name": false, "date": false, "name_msg": "", "date_msg": ""}
        this.clearErrorMsgs()
        this.engagementName = ''
        this.engagementDesc = ''
        this.application = null
        this.engagementDateRange = ''
        this.$refs.createEngagementModal.show()
      },
      closeCreateEngagement() {
        this.$refs.createEngagementModal.hide()
      },
      clearErrorMsgs() {
        this.error_msgs['name'] = false
        this.error_msgs['date'] = false
        this.error_msgs['app'] = false
        this.error_msgs['type'] = false
        this.error_msgs['desc'] = false
      },
      submitCreateEngagement() {
        if (this.org && this.token) {
          const dayOne = new Date(this.engagementDateRange[0])
          const d = dayOne.getDate()
          const m = dayOne.getMonth() + 1
          const y = dayOne.getFullYear()
          const dayTwo = new Date(this.engagementDateRange[1])
          const d1 = dayTwo.getDate()
          const m1 = dayTwo.getMonth() + 1
          const y1 = dayTwo.getFullYear()
          const startDate = y + '-' + (m <= 9 ? '0' + m : m) + '-' + (d <= 9 ? '0' + d : d)
          const stopDate = y1 + '-' + (m1 <= 9 ? '0' + m1 : m1) + '-' + (d1 <= 9 ? '0' + d1 : d1)
          const form_data = new FormData()
          form_data.append('name', this.engagementName)
          form_data.append('description', this.engagementDesc)
          form_data.append('application', this.application.value)
          form_data.append('start_date', startDate)
          form_data.append('stop_date', stopDate)
          axios.put('/engagements/', form_data)
            .then(res => {
              this.$refs.createEngagementModal.hide()
              this.isLoading = false
              this.$notify({
                group: 'foo',
                type: 'success',
                title: 'success',
                text: 'The engagement has been created successfully!',
                position: 'top right'
              })
              this.$router.go()
            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
                  notValidUser()
                  this.$router.push('/')
                }
            if (error.response.status === 404) {
              this.$router.push('/not_found')
            }
            else if (error.response.status === 403) {
              this.$router.push('/forbidden')
            }
            else if (error.response.status === 400) {
              // if(error.response.data.name){
              //     this.error_msgs['name'] = true
              //     this.error_msgs['name_msg'] = 'engagement with this name already exists.'
              //   }
              //   else{
              //        this.error_msgs['name'] = false
              //   }
              //   if(error.response.data.non_field_errors){
              //     this.error_msgs['date'] = true
              //     this.error_msgs['date_msg'] = 'Stop date must occur after start date'
              //   }
              //   else{
              //        this.error_msgs['date'] = false
              //   }

              // this.$router.push('/forbidden')


              if (error.response.data['name']) {
                this.error_msgs['name'] = true
                this.error_msgs['name_msg'] = error.response.data['name'][0]
              }
              if (error.response.data['start_date'] || error.response.data['stop_date'] || error.response.data['non_field_errors']) {
                this.error_msgs['date'] = true
                this.error_msgs['date_msg'] = 'Stop date must occur after start date'
                if (error.response.data['start_date'][0] || error.response.data['stop_date'][0]) {
                  this.error_msgs['date_msg'] = error.response.data['start_date'][0] + '\n' + error.response.data['stop_date'][0]
                }
              }
              if (error.response.data['description']) {
                this.error_msgs['desc'] = true
                this.error_msgs['desc_msg'] = error.response.data['description'][0]
              }
              if (error.response.data['application']) {
                this.error_msgs['app'] = true
                this.error_msgs['app_msg'] = error.response.data['application'][0]
              }
            }
            else {
              this.$router.push('/error')
            }
          })
        } else {
          notValidUser()
          this.$router.push('/')
        }
      },
      updateEngagement(event) {
        this.clearErrorMsgs()
        this.engagementId = event.id
        this.error_msgs = {"name": false, "date": false, "name_msg": "", "date_msg": ""}
        if (this.org && this.token && this.engagementId) {
          this.$refs.updateEngagementModal.show()
          axios.get('/engagements/' + this.engagementId + '/')
            .then(res => {
              this.updateEngagementName = res.data.name
              this.updateEngagementDesc = res.data.description
              this.updateEngagementDateRange = [res.data.start_date, res.data.stop_date]
              for (const appVal of this.applicationOption) {
                if (res.data.application === appVal.value) {
                  this.updateApplication = appVal.label
                  this.updateApplication = {'label': appVal.label, 'value': res.data.application}
                }
              }

            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
                  notValidUser()
                  this.$router.push('/')
                }
            if (error.res.status === 404) {
              this.$router.push('/not_found')
            } else if (error.res.status === 404) {
              this.$router.push('/forbidden')
            } else {
              this.$router.push('/error')
            }
          })
        } else {
          notValidUser()
          this.$router.push('/')
        }
      },
      closeUpdateEngagement() {
        this.$refs.updateEngagementModal.hide()
      },
      submitUpdateEngagement() {
        if (this.org && this.token && this.engagementId) {
          const dayOne = new Date(this.updateEngagementDateRange[0])
          const d = dayOne.getDate()
          const m = dayOne.getMonth() + 1
          const y = dayOne.getFullYear()
          const dayTwo = new Date(this.updateEngagementDateRange[1])
          const d1 = dayTwo.getDate()
          const m1 = dayTwo.getMonth() + 1
          const y1 = dayTwo.getFullYear()
          const startDate = y + '-' + (m <= 9 ? '0' + m : m) + '-' + (d <= 9 ? '0' + d : d)
          const stopDate = y1 + '-' + (m1 <= 9 ? '0' + m1 : m1) + '-' + (d1 <= 9 ? '0' + d1 : d1)
          const formData = {
            'name': this.updateEngagementName,
            'description': this.updateEngagementDesc,
            'application': this.updateApplication.value,
            'start_date': startDate,
            'stop_date': stopDate
          }
          axios.post('/engagements/' + this.engagementId + '/', formData)
            .then(res => {
              this.$refs.updateEngagementModal.hide()
              this.isLoading = true
              this.$notify({
                group: 'foo',
                type: 'info',
                title: 'success',
                text: 'The engagement has been updated successfully!',
                position: 'top right'
              })
              this.$router.go()
              this.engagementId = ''
            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
                  notValidUser()
                  this.$router.push('/')
                }
            if (error.response.status === 404) {
              this.$router.push('/not_found')
            }
            else if (error.response.status === 403) {
              this.$router.push('/forbidden')
            }
            else if (error.response.status === 400) {

              if (error.response.data['name']) {
                this.error_msgs['name'] = true
                this.error_msgs['name_msg'] = error.response.data['name'][0]
              }
              if (error.response.data['start_date'] || error.response.data['stop_date'] || error.response.data['non_field_errors']) {
                this.error_msgs['date'] = true
                this.error_msgs['date_msg'] = 'Stop date must occur after start date'
                if (error.response.data['start_date'][0] || error.response.data['stop_date'][0]) {
                  this.error_msgs['date_msg'] = error.response.data['start_date'][0] + '\n' + error.response.data['stop_date'][0]
                }
              }
              if (error.response.data['description']) {
                this.error_msgs['desc'] = true
                this.error_msgs['desc_msg'] = error.response.data['description'][0]
              }
              if (error.response.data['application']) {
                this.error_msgs['app'] = true
                this.error_msgs['app_msg'] = error.response.data['application'][0]
              }
              if (error.response.data['bucket']) {
                this.error_msgs['type'] = true
                this.error_msgs['type_msg'] = error.response.data['bucket'][0]
              }


              // if(error.response.data.name){
              //     this.error_msgs['name'] = true
              //     this.error_msgs['name_msg'] = 'engagement with this name already exists.'
              //   }
              //   else{
              //        this.error_msgs['name'] = false
              //   }
              //   if(error.response.data.non_field_errors){
              //     this.error_msgs['date'] = true
              //     this.error_msgs['date_msg'] = 'Stop date must occur after start date'
              //   }
              //   else{
              //        this.error_msgs['date'] = false
              //   }
              // this.$router.push('/forbidden')
            }
            else {
              this.$router.push('/error')
            }
          })
        } else {
          notValidUser()
          this.$router.push('/')
        }
      },
      deleteEngagement(event) {
        this.engagementId = event.id
        this.$refs.deleteEngagementModal.show()
      },
      closeDeleteEngagement() {
        this.$refs.deleteEngagementModal.hide()
      },
      submitDeleteEngagement() {
        if (this.org && this.token && this.engagementId) {
          axios.delete('/engagements/' + this.engagementId + '/')
            .then(res => {
              this.$refs.deleteEngagementModal.hide()
              this.isLoading = true
              this.$notify({
                group: 'foo',
                type: 'success',
                title: 'success',
                text: 'The engagement has been deleted successfully!',
                position: 'top right'
              })
              this.$router.go()
              this.engagementId = ''
            }).catch(error => {
            if (error.response.data.detail === 'Signature has expired.'){
                  notValidUser()
                  this.$router.push('/')
                }
            if (error.res.status === 404) {
              this.$router.push('/not_found')
            } else if (error.res.status === 404) {
              this.$router.push('/forbidden')
            } else {
              this.$router.push('/error')
            }
          })
        } else {
          notValidUser()
          this.$router.push('/')
        }
      }
    }
  }
</script>

<style scoped>
  .btn-orange-close {
    color: #ff542c;
    background-color: #FFFFFF;
    border-color: #ff542c;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;
  }

  .btn-orange-close:focus,
  .btn-orange-close.focus {
    color: #ff542c;
    background-color: #FFFFFF;
    border-color: #ff542c;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;
  }

  .btn-orange-close:hover {
    color: #FFFFFF;
    background-color: #ff542c;
    border-color: #FFFFFF;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;
  }

  .btn-orange-submit {
    color: #FFFFFF;
    background-color: #ff542c;
    border-color: #FFFFFF;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;

  }

  .btn-orange-submit:focus,
  .btn-orange-submit.focus {
    color: #FFFFFF;
    background-color: #ff542c;
    border-color: #FFFFFF;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;
  }

  .btn-orange-submit:hover {
    color: #FFFFFF;
    background-color: #ff542c;
    border-color: #FFFFFF;
    font-family: 'Avenir';
    border-radius: 14px;
    padding: 3px 12px;
    margin-bottom: 0;
    font-size: 14px;
  }

  .label {
    font-family: 'Avenir';
    font-size: 16px;
    line-height: 1.33;
    color: #000000;
  }

  .inline-form-control {
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    outline: none;
    width: 100%;
    /*padding: 7px;*/
    padding: 7px 30px 7px 7px;
    border: none;
    border-bottom: 1px solid #ddd;
    background: transparent;
    margin-bottom: 10px;
    font: 16px 'Avenir';
    height: 45px;
    position: relative;
    display: inline-block;
  }

  .delete-header {
    font-family: 'Avenir';
    font-size: 16px;
    font-weight: 500;
    line-height: 0.99;
    text-align: center;
    color: #232325;
  }

  .error {
    font-family: 'Avenir';
    font-size: 16px;
    font-weight: 400;
    line-height: 0.99;
    text-align: center;
    color: #f44336;
  }
  #input_count {
    position:absolute;
    bottom:2px;
    right:15px;
    width:24px;
    height:24px;
    /*color: #909090;*/
    color: green;
    font-size: 14px;
}
</style>
