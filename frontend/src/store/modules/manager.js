/*
 * @Description: 
 * @Author: l
 * @Date: 2021-06-03 14:01:04
 * @LastEditors: l
 * @LastEditTime: 2021-06-26 16:45:37
 * @FilePath: \DistributedControlSystem\frontend\src\store\modules\manager.js
 */

const api = '/api/manager';
import axios from 'axios'
export default {
    state: {
        startTime: '',
        endTime: '',
        reportIsOk: false,
        report:[]
    },
    getter: {},
    mutations: {
        setReportIsOk(state, isOK) {
            state.reportIsOk = isOK;
        },
        setStartTime(state, startTime) {
            state.startTime = startTime;
        },
        setEndTime(state, endTime) {
            state.endTime = endTime;
        },
        setReport(state, report) {
            state.report=report;
        },

    },
    actions: {
        checkReport({ commit }, payload) {
            console.log('checkReport...');
            return axios.post(api + '/checkReport', {
                startTime: payload.startTime,
                endTime: payload.endTime,
            }).then((response) => {
                if (response.data.error == false) {
                    commit('setStartTime', payload.startTime);
                    commit('setEndTime', payload.endTime);
                    commit('setReportIsOk', true);
                    commit('setReport', response.data.report);
                } else {
                    commit('setReprotIsOk', false);
                }
            }).catch((error) => {
                console.error(error)
            });
        }
    },
    modules: {},
    namespaced: true,
}