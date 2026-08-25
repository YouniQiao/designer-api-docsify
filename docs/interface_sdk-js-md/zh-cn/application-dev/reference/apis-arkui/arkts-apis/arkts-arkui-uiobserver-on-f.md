# on

## 导入模块

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## on('navDestinationUpdate')

```TypeScript
export function on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<NavDestinationInfo>): void
```

监听NavDestination组件的状态变化。与  
* uiObserver.on相比，新增了options参数，即支持指定监听的Navigation的id。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'navDestinationUpdate' | 是 |
| options | { navigationId: ResourceStr } | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | 是 |


## on('navDestinationUpdate')

```TypeScript
export function on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void
```

监听NavDestination组件的状态变化。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'navDestinationUpdate' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NavDestinationInfo&gt; | 是 |


## on('scrollEvent')

```TypeScript
export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'scrollEvent' | 是 |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md)&gt; | 是 |


## on('scrollEvent')

```TypeScript
export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'scrollEvent' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScrollEventInfo](arkts-arkui-uiobserver-scrolleventinfo-i.md)&gt; | 是 |


## on('routerPageUpdate')

```TypeScript
export function on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void
```

监听router中page页面的状态变化。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'routerPageUpdate' | 是 |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;RouterPageInfo&gt; | 是 |


## on('densityUpdate')

```TypeScript
export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void
```

监听屏幕像素密度变化。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'densityUpdate' | 是 |
| context | [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md)&gt; | 是 |


## on('willDraw')

```TypeScript
export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void
```

监听每一帧绘制指令下发情况。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'willDraw' | 是 |
| context | [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |


## on('didLayout')

```TypeScript
export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void
```

监听每一帧布局完成情况。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'didLayout' | 是 |
| context | [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |


## on('tabContentUpdate')

```TypeScript
export function on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void
```

监听指定Tabs组件id的TabContent页面切换事件。相比on('tabChange')，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'tabContentUpdate' | 是 |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md)&gt; | 是 |


## on('tabContentUpdate')

```TypeScript
export function on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void
```

监听TabContent页面的切换事件。相比on('tabChange')，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'tabContentUpdate' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[TabContentInfo](arkts-arkui-uiobserver-tabcontentinfo-i.md)&gt; | 是 |


## on('navDestinationSwitch')

```TypeScript
export function on(
    type: 'navDestinationSwitch',
    context: UIAbilityContext | UIContext,
    callback: Callback<NavDestinationSwitchInfo>
  ): void
```

监听Navigation的页面切换事件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'navDestinationSwitch' | 是 |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | 是 |


## on('navDestinationSwitch')

```TypeScript
export function on(
    type: 'navDestinationSwitch',
    context: UIAbilityContext | UIContext,
    observerOptions: NavDestinationSwitchObserverOptions,
    callback: Callback<NavDestinationSwitchInfo>
  ): void
```

监听Navigation的页面切换事件。与uiObserver.on相比，新增了observerOptions参数，即支持设置监听选项。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'navDestinationSwitch' | 是 |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) \| [UIContext](../arkts-components/arkts-arkui-uicontext-t.md) | 是 |
| observerOptions | [NavDestinationSwitchObserverOptions](arkts-arkui-uiobserver-navdestinationswitchobserveroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NavDestinationSwitchInfo](arkts-arkui-uiobserver-navdestinationswitchinfo-i.md)&gt; | 是 |
