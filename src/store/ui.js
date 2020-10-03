const state = () => ({
  tabs: {
    gameBar: [
      { name: 'main', title: 'Game', active: true },
      { name: 'history', title: 'History' },
      { name: 'settings', title: 'Settings' }      
    ],
    handBar: [
      { name: 'fold', title: 'Fold', active: true },
      { name: 'check', title: 'Check' },
      { name: 'call', title: 'Call' },
      { name: 'raise', title: 'Raise' },
    ]
  }
})

const actions = {
  setTab({ commit }, { tab, tabId }) {
    commit('setTab', { tab, tabId })
  }
}

const mutations = {
  setTab(state, { tab, tabId }) {
    state.tabs[tabId] = state.tabs[tabId].map(el => Object.assign({}, el, { active: tab.name === el.name }))
  }
}

const getters = {
  activeTabName(state) {
    return tabId => {
      return state.tabs[tabId].find(el => el.active).name
    }
  },
  activeGameBarTab(state, getters) {
    return getters.activeTabName('gameBar')
  },
  activeHandBarTab(state, getters) {
    return getters.activeTabName('handBar')
  },
  tabsById(state) {
    return tabId => {
      return state.tabs[tabId]
    }
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
}
