const state = () => ({
  gameBarTab: 'main',
  gameBarTabs: [
    { name: 'main', title: 'Game', active: true },
    { name: 'history', title: 'History' },
    { name: 'settings', title: 'Settings' }
  ],
  handBarTab: 'fold',
  handBarTabs: [
    { name: 'fold', title: 'Fold', active: true },
    { name: 'check', title: 'Check' },
    { name: 'call', title: 'Call' },
    { name: 'raise', title: 'Raise' },
  ]
})

const actions = {
  gameBarSetTab({ commit }, tab) {
    commit('gameBarSetTab', tab)
  },
  handBarSetTab({ commit }, tab) {
    commit('handBarSetTab', tab)
  }
}

const mutations = {
  gameBarSetTab(state, tab) {
    state.gameBarTab = tab.name
    state.gameBarTabs = state.gameBarTabs.map(el => Object.assign({}, el, { active: tab.name === el.name }))
  },
  handBarSetTab(state, tab) {
    state.handBarTab = tab.name
    state.handBarTabs = state.handBarTabs.map(el => Object.assign({}, el, { active: tab.name === el.name }))
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}
