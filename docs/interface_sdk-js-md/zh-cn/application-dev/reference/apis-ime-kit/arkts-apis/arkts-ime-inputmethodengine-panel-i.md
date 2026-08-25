# Panel

Panel是输入法面板对象，提供面板页面加载、显示/隐藏、尺寸调整、位置移动、模式切换等功能。Panel实例通过InputMethodAbility的 [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) 接口获取，使用完毕后需调用 [destroyPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#destroypanel) 销毁以释放资源。createPanel与destroyPanel必须配对调用。 核心功能概述：   
- 页面加载：通过[setUiContent](#setuicontent)为面板 加载键盘页面内容，支持加载普通页面和与LocalStorage关联的页面。   
- 显示与隐藏：通过[show](#show)显示面板，通过 [hide](#hide)隐藏面板。面板的显示/隐藏也可通过订阅on('show')/on('hide')事件 监听状态变化。   
- 尺寸与位置调整：通过 [resize](#resize)调整面板尺寸，通过 [moveTo](#moveto)移动面板位置，通过 [startMoving](#startmoving)拖拽移动面板，通过 [adjustPanelRect](#adjustpanelrect)/ [updatePanelRect](#updatepanelrect)/ [updateRegion](#updateregion)调整面板区域。   
- 模式设置：通过[changeFlag](#changeflag)切换面板固定态/浮动态，通过 [setPrivacyMode](#setprivacymode)设置隐私模式，通过 [setImmersiveMode](#setimmersivemode)/ [getImmersiveMode](#getimmersivemode)设置/获取沉浸模式。   
- 事件监听：通过on('show')/on('hide')/on('sizeChange')监听面板状态变化事件。   
 面板生命周期： 
1. 在InputMethodAbility的[createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel)中创建Panel实例并指定面板类型和标志位。 
2. 调用[setUiContent](#setuicontent)加载键盘页面内容。 
3. 调用[show](#show)显示面板，用户可交互。 
4. 根据需要调用resize、moveTo、changeFlag等接口动态调整面板。 
5. 使用完毕后调用[destroyPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#destroypanel)销毁面板，释放资源。 
 下列API均需使用 [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) 获取到Panel实例后，通过实例调用。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: PanelRect): void
```

预设置输入法应用横竖屏大小。接口调用完毕表示adjust请求已提交到输入法框架，不表示执行完毕。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。
   
> 
   
> 此接口为同步接口，接口返回成功仅代表系统侧收到设置的请求，不代表设置完成。如果需要感知执行过程中的异常，建议使用
   
> [updatePanelRect](#updatepanelrect)或
   
> [updatePanelRectSync](#updatepanelrectsync)。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。此接口兼容
   
> [adjustPanelRect](#adjustpanelrect)的调用方法，若入参rect
   
> 仅填写属性landscapeRect和portraitRect，则默认调用
   
> [adjustPanelRect](#adjustpanelrect)。
   
> 
   
> 此接口为同步接口，接口返回成功仅代表系统侧收到设置的请求，不代表设置完成。如果需要感知执行过程中的异常，建议使用
   
> [updatePanelRect](#updatepanelrect)或
   
> [updatePanelRectSync](#updatepanelrectsync)
   
> 。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。
   
> 
   
> 当com.ohos.sceneboard进程不存在时，输入法热区生效范围保持和软键盘区域一致。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |

## changeFlag

```TypeScript
changeFlag(flag: PanelFlag): void
```

将输入法应用的面板状态改变为其他[PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md)形态，仅对 [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md)生效。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

获取当前窗口的displayId，使用Promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## getImmersiveMode

```TypeScript
getImmersiveMode(): ImmersiveMode
```

获取输入法应用的沉浸模式。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-immersivemode-t.md) |

## getSystemPanelCurrentInsets

```TypeScript
getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>
```

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。

**起始版本：** 21

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SystemPanelInsets](arkts-ime-inputmethodengine-systempanelinsets-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800022](../errorcode-inputmethod-framework.md#12800022-无效的displayid) |

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

隐藏当前输入法面板，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## hide

```TypeScript
hide(): Promise<void>
```

隐藏当前输入法面板，使用promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## moveTo

```TypeScript
moveTo(x: number, y: number, callback: AsyncCallback<void>): void
```

移动面板位置，使用callback异步回调。[面板状态](arkts-ime-inputmethodengine-panelflag-e.md)为固定态时，不产生实际移动效果。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

移动面板位置，使用promise异步回调。[面板状态](arkts-ime-inputmethodengine-panelflag-e.md)为固定态时，不产生实际移动效果。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('show')

```TypeScript
off(type: 'show', callback?: () => void): void
```

取消监听当前面板的显示状态，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'show' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('hide')

```TypeScript
off(type: 'hide', callback?: () => void): void
```

取消监听当前面板的隐藏状态，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hide' | 是 |
| callback | () = & gt; void | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('sizeChange')

```TypeScript
off(type: 'sizeChange', callback?: SizeChangeCallback): void
```

取消监听当前面板大小变化，使用callback异步回调。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景
   
> ），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。
   
> 
   
> - 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)类型的必选参数。
   
> 
   
> - 从API version 15起，调用
   
> [adjustPanelRect](#adjustpanelrect)接口后，此
   
> 接口回调函数增加[KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md)类型的可选参数。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sizeChange' | 是 |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 否 |

## on('show')

```TypeScript
on(type: 'show', callback: () => void): void
```

监听当前面板显示状态，使用 callback 异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'show' | 是 |
| callback | () = & gt; void | 是 |

## on('hide')

```TypeScript
on(type: 'hide', callback: () => void): void
```

监听当前面板隐藏状态，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hide' | 是 |
| callback | () = & gt; void | 是 |

## on('sizeChange')

```TypeScript
on(type: 'sizeChange', callback: SizeChangeCallback): void
```

监听当前面板大小变化，使用callback异步回调。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。输入法通过adjustPanelRect等接口对面板大小进行调节时，系统会根据一定规则校验计算出最终的数值（例如超出屏幕等场景
   
> ），输入法应用可通过该回调获取的真实面板大小，完成最终的面板布局刷新。
   
> 
   
> - 从API version 12-14开始支持，此接口回调函数中仅包含[window.Size](../../apis-arkui/arkts-apis/arkts-arkui-window-size-i.md)类型的必选参数。
   
> 
   
> - 从API version 15起，调用
   
> [adjustPanelRect](#adjustpanelrect)接口后，此
   
> 接口回调函数增加[KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md)类型的可选参数。

**起始版本：** 12

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sizeChange' | 是 |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 是 |

## resize

```TypeScript
resize(width: number, height: number, callback: AsyncCallback<void>): void
```

改变当前输入法面板的大小，使用callback异步回调。   
> **说明：**
   
> 
   
> 面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## resize

```TypeScript
resize(width: number, height: number): Promise<void>
```

改变当前输入法面板的大小，使用Promise异步回调。   
> **说明：**
   
> 
   
> 面板宽度不超出屏幕宽度，面板高度不高于屏幕高度的0.7倍。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setImmersiveEffect

```TypeScript
setImmersiveEffect(effect: ImmersiveEffect): void
```

设置输入法应用的沉浸效果。   
- 只有在[启用沉浸式模式](#setimmersivemode)时，才能使用渐变模式和流光模式。   
- 只有在启用渐变模式时，才能使用流光模式。   
- 未启用渐变模式时，渐变高度必须为0px。   
- 只有系统应用才能设置流光模式。   
- 必须先调用以下任一接口，才能调用当前接口：   
 - [adjustPanelRect](#adjustpanelrect)(支持API version 12)   
 - [adjustPanelRect](#adjustpanelrect)(支持 API version 15)   
 - [resize](#resize)(支持API version 10)

**起始版本：** 20

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [ImmersiveEffect](arkts-ime-inputmethodengine-immersiveeffect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800020](../errorcode-inputmethod-framework.md#12800020-沉浸效果参数配置错误) |
| [12800021](../errorcode-inputmethod-framework.md#12800021-调用顺序错误) |

## setImmersiveMode

```TypeScript
setImmersiveMode(mode: ImmersiveMode): void
```

设置输入法应用的沉浸模式。只能设置为不使用沉浸模式(NONE_IMMERSIVE)、浅色沉浸模式(LIGHT_IMMERSIVE)或深色沉浸模式(DARK_IMMERSIVE)。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-immersivemode-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

设置屏幕常亮。使用Promise异步回调。   
> **说明:**
   
> 
   
> - 当键盘拉起时设置常亮生效，键盘关闭则自动失效。
   
> 
   
> - 规范使用该接口：必要场景（例如：语音输入）下，设置该属性为true；退出必要场景后，重置该属性为false；其他场景下，不使用该接口。

**起始版本：** 20

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isKeepScreenOn](../../apis-arkui/arkts-apis/arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean): void
```

将输入法应用的面板设置为隐私模式，隐私模式不可被录屏、截屏。

**起始版本：** 11

**需要权限：** ohos.permission.PRIVACY_WINDOW

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](../../apis-arkui/arkts-apis/arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setSystemPanelButtonColor

```TypeScript
setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>
```

设置当前面板功能键颜色和功能键的背景颜色。使用Promise异步回调。

**起始版本：** 22

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fillColor | string \| undefined | 是 |
| backgroundColor | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## setUiContent

```TypeScript
setUiContent(path: string, callback: AsyncCallback<void>): void
```

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

为当前的输入法面板加载具体页面内容，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

为当前的输入法面板加载与LocalStorage相关联的具体页面内容，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage): Promise<void>
```

为当前面板加载与LocalStorage相关联的具体页面内容，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## show

```TypeScript
show(callback: AsyncCallback<void>): void
```

显示当前输入法面板，使用callback异步回调。输入法应用与编辑框绑定成功后可正常调用。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## show

```TypeScript
show(): Promise<void>
```

显示当前输入法面板，使用promise异步回调。输入法应用与编辑框绑定成功后可正常调用。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## startMoving

```TypeScript
startMoving(): void
```

发送移动命令给窗口，使面板进入可拖动状态。不产生实际移动效果，仅在用户通过鼠标拖动面板时才会移动。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

| 错误码ID |
| --- |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>
```

预设置输入法应用横竖屏大小。使用Promise异步回调。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。
   
> 
   
> 此接口为异步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。使用Promise异步回调。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。此接口兼容
   
> [adjustPanelRect](#adjustpanelrect)的调用方法，若入参rect
   
> 仅填写属性landscapeRect和portraitRect，则默认调用
   
> [adjustPanelRect](#adjustpanelrect)。
   
> 
   
> 此接口为异步接口，接口返回仅代表系统侧收到设置的请求，不代表已完成设置。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。
   
> 
   
> 当com.ohos.sceneboard进程不存在时，输入法热区生效范围保持和软键盘区域一致。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void
```

预设置输入法应用横竖屏大小。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [updatePanelRect](#updatepanelrect)。
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。
   
> 
   
> 此接口为同步接口，接口返回代表系统侧收到设置的请求，并已完成设置。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [PanelRect](arkts-ime-inputmethodengine-panelrect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。   
> **说明：**
   
> 
   
> 同步接口阻塞主线程，容易影响UI交互，需谨慎使用。建议优先使用对应的异步接口
   
> [updatePanelRect](#updatepanelrect)。
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。此接口兼容
   
> [adjustPanelRect](#adjustpanelrect)的调用方法，若入参rect
   
> 仅填写属性landscapeRect和portraitRect，则默认调用
   
> [adjustPanelRect](#adjustpanelrect)。
   
> 
   
> 此接口为同步接口，接口返回代表系统侧收到设置的请求，并已完成设置。
   
> 
   
> 手机的PanelFlag是FLG_FLOATING且面板宽度在0~288vp之间时，面板底部功能键将随面板宽度动态调整大小，为了保证最佳用户体验，建议面板宽度不小于90vp。
   
> 
   
> 当com.ohos.sceneboard进程不存在时，输入法热区生效范围保持和软键盘区域一致。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |

## updateRegion

```TypeScript
updateRegion(inputRegion: Array<window.Rect>): void
```

更新当前状态下输入法面板内的热区。   
> **说明:**
   
> 
   
> 仅用于SOFT_KEYBOARD类型，状态为FLG_FIXED或FLG_FLOATING的面板。
   
> 
   
> 此接口为同步接口，接口返回仅代表系统侧收到更新热区的请求，不代表已完成热区更新。
   
> 
   
> 当com.ohos.sceneboard进程不存在时，输入法热区生效范围保持和软键盘区域一致。

**起始版本：** 15

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputRegion | Array & lt;window.Rect & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
