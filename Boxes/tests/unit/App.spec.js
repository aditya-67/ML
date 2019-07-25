import { shallowMount } from '@vue/test-utils'
import App from '@/App'

describe('App', () => {
  it('passing test', () => {
    expect(true).toBeTruthy()
  })

  it('failing test', () => {
    expect(false).toBeFalsy()
  })
  test('is a Vue instance', () => {
    const wrapper = shallowMount(App)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  test('renders correctly', () => {
    const wrapper = shallowMount(App)
    expect(wrapper.element).toMatchSnapshot()
  })
})
