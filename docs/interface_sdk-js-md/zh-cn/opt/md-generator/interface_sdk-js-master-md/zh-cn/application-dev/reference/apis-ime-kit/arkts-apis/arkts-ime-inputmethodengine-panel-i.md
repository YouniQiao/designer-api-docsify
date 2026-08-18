# Panel

Panel是输入法面板对象，提供面板页面加载、显示/隐藏、尺寸调整、位置移动、模式切换等功能。Panel实例通过InputMethodAbility的 [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) 接口获取，使用完毕后需调用 [destroyPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#destroypanel) 销毁以释放资源。createPanel与destroyPanel必须配对调用。 **核心功能概述：** - **页面加载**：通过 [setUiContent](#setuicontent)为面板加载键盘页面内容， 支持加载普通页面和与LocalStorage关联的页面。 - **显示与隐藏**：通过[show](#show)显示面板，通过 [hide](#hide)隐藏面板。面板的显示/隐藏也可通过订阅on('show')/on('hide')事件 监听状态变化。 - **尺寸与位置调整**：通过 [resize](#resize)调整面板尺寸，通过 [moveTo](#moveto)移动面板位置，通过 [startMoving](#startmoving)拖拽移动面板，通过 [adjustPanelRect](#adjustpanelrect)/ [updatePanelRect](#updatepanelrect)/ [updateRegion](#updateregion)调整面板区域。 - **模式设置**：通过[changeFlag](#changeflag)切换面板固定态/浮动态，通过 [setPrivacyMode](#setprivacymode)设置隐私模式，通过 [setImmersiveMode](#setimmersivemode)/ [getImmersiveMode](#getimmersivemode)设置/获取沉浸模式。 - **事件监听**：通过on('show')/on('hide')/on('sizeChange')监听面板状态变化事件。 **面板生命周期：** 1. 在InputMethodAbility的[createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel)中创建Panel实例并指定面板类型和标志位。 2. 调用[setUiContent](#setuicontent)加载键盘页面内容。 3. 调用[show](#show)显示面板，用户可交互。 4. 根据需要调用resize、moveTo、changeFlag等接口动态调整面板。 5. 使用完毕后调用[destroyPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#destroypanel)销毁面板，释放资源。 下列API均需使用 [createPanel](arkts-ime-inputmethodengine-inputmethodability-i.md#createpanel) 获取到Panel实例后，通过实例调用。

**起始版本：** 23

<!--Device-inputMethodEngine-interface Panel--><!--Device-inputMethodEngine-interface Panel-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
```

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: PanelRect): void
```

预设置输入法应用横竖屏大小。接口调用完毕表示adjust请求已提交到输入法框架，不表示执行完毕。

**起始版本：** 23

<!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: PanelRect): void--><!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: PanelRect): void-End-->

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

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

// 定义横屏状态下面板的矩形区域
let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

// 定义竖屏状态下面板的矩形区域
let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

// 设置面板状态为固定态
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 配置面板的横竖屏矩形区域
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
// 预设置输入法应用横竖屏大小
panel.adjustPanelRect(panelFlag, panelRect);
```

## adjustPanelRect

```TypeScript
adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。

**起始版本：** 23

<!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void--><!--Device-Panel-adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void-End-->

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
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];
// 目标面板状态类型。
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.adjustPanelRect(panelFlag, panelRect);
```

## changeFlag

```TypeScript
changeFlag(flag: PanelFlag): void
```

将输入法应用的面板状态改变为其他[PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md#panelflag)形态，仅对 [SOFT_KEYBOARD](arkts-ime-inputmethodengine-paneltype-e.md#paneltype)生效。

**起始版本：** 23

<!--Device-Panel-changeFlag(flag: PanelFlag): void--><!--Device-Panel-changeFlag(flag: PanelFlag): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
panel.changeFlag(panelFlag);
```

## getDisplayId

```TypeScript
getDisplayId(): Promise<number>
```

获取当前窗口的所在id，使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-getDisplayId(): Promise<long>--><!--Device-Panel-getDisplayId(): Promise<long>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.getDisplayId().then((result: number) => {
  console.info('get displayId:' + result);
}).catch((err: BusinessError) => {
  console.error(`Failed to get displayId. Code is ${err.code}, message is ${err.message}`);
});
```

## getImmersiveMode

```TypeScript
getImmersiveMode(): ImmersiveMode
```

获取输入法应用的沉浸模式。

**起始版本：** 23

<!--Device-Panel-getImmersiveMode(): ImmersiveMode--><!--Device-Panel-getImmersiveMode(): ImmersiveMode-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| [ImmersiveMode](../../apis-arkui/arkts-apis/arkts-arkui-immersivemode-t.md) |

**示例**

```TypeScript
let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();
```

## getSystemPanelCurrentInsets

```TypeScript
getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>
```

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。

**起始版本：** 21

<!--Device-Panel-getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>--><!--Device-Panel-getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>-End-->

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
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800022](../errorcode-inputmethod-framework.md#12800022-无效的displayid) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
let panelConfig: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG_FIXED
}
// 以下逻辑需要在输入法InputMethodExtensionAbility中执行，this.context是InputMethodExtensionAbility的上下文
// 创建输入法面板
inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
  panel.getDisplayId().then((displayId: number) => {
    panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
      console.info(`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }`);
    }).catch((error: BusinessError) => {
      console.error(`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}`);
    })
  });
})
```

## getSystemPanelCurrentInsets

```TypeScript
getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets | null>
```

获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。使用Promise异步回调。 &lt;p&gt;仅支持悬浮或固定键盘.&lt;/p&gt; &lt;p&gt;获取指定屏幕当前状态（例如：折叠或展开）下，当前输入法键盘状态（例如：悬浮或固定）下输入法软键盘相对系统面板的偏移区域。&lt;/p&gt; &lt;p&gt;当屏幕状态发生变化，需要重新获取偏移区域。&lt;/p&gt;

**起始版本：** 23

<!--Device-Panel-getSystemPanelCurrentInsets(displayId: long): Promise<SystemPanelInsets | null>--><!--Device-Panel-getSystemPanelCurrentInsets(displayId: long): Promise<SystemPanelInsets | null>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SystemPanelInsets](arkts-ime-inputmethodengine-systempanelinsets-i.md) \| null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800022](../errorcode-inputmethod-framework.md#12800022-无效的displayid) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

隐藏当前输入法面板，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-hide(callback: AsyncCallback<void>): void--><!--Device-Panel-hide(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding the panel.');
});
```

## hide

```TypeScript
hide(): Promise<void>
```

隐藏当前输入法面板，使用promise异步回调。

**起始版本：** 23

<!--Device-Panel-hide(): Promise<void>--><!--Device-Panel-hide(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide panel. Code is ${err.code}, message is ${err.message}`);
});
```

## moveTo

```TypeScript
moveTo(x: number, y: number, callback: AsyncCallback<void>): void
```

移动面板位置，使用callback异步回调。[面板状态](arkts-ime-inputmethodengine-panelflag-e.md#panelflag)为固定态时，不产生实际移动效果。

**起始版本：** 23

<!--Device-Panel-moveTo(x: int, y: int, callback: AsyncCallback<void>): void--><!--Device-Panel-moveTo(x: int, y: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 移动输入法面板位置
panel.moveTo(300, 300, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving the panel.');
});
```

## moveTo

```TypeScript
moveTo(x: number, y: number): Promise<void>
```

移动面板位置，使用promise异步回调。[面板状态](arkts-ime-inputmethodengine-panelflag-e.md#panelflag)为固定态时，不产生实际移动效果。

**起始版本：** 23

<!--Device-Panel-moveTo(x: int, y: int): Promise<void>--><!--Device-Panel-moveTo(x: int, y: int): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 移动输入法面板位置
panel.moveTo(300, 300).then(() => {
  console.info('Succeeded in moving the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to move panel. Code is ${err.code}, message is ${err.message}`);
});
```

## offHide

```TypeScript
offHide(callback?: Callback<void>): void
```

取消监听当前面板隐藏状态，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-offHide(callback?: Callback<void>): void--><!--Device-Panel-offHide(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## offShow

```TypeScript
offShow(callback?: Callback<void>): void
```

取消监听当前输入法面板的隐藏状态，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-offShow(callback?: Callback<void>): void--><!--Device-Panel-offShow(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

## offSizeChange

```TypeScript
offSizeChange(callback?: SizeChangeCallback): void
```

取消监听当前面板大小变化，使用callback异步回调。 &lt;p&gt;此接口仅支持固定或悬浮态的软键盘类型Panel。&lt;/p&gt;

**起始版本：** 23

<!--Device-Panel-offSizeChange(callback?: SizeChangeCallback): void--><!--Device-Panel-offSizeChange(callback?: SizeChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 否 |

## off_hide

```TypeScript
off(type: 'hide', callback?: () => void): void
```

取消监听当前面板的隐藏状态，使用callback异步回调。

**起始版本：** 10

<!--Device-Panel-off(type: 'hide', callback?: () => void): void--><!--Device-Panel-off(type: 'hide', callback?: () => void): void-End-->

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

**示例**

```TypeScript
panel.off('hide');
```

## off_show

```TypeScript
off(type: 'show', callback?: () => void): void
```

取消监听当前面板的显示状态，使用callback异步回调。

**起始版本：** 10

<!--Device-Panel-off(type: 'show', callback?: () => void): void--><!--Device-Panel-off(type: 'show', callback?: () => void): void-End-->

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

**示例**

```TypeScript
panel.off('show');
```

## off_sizeChange

```TypeScript
off(type: 'sizeChange', callback?: SizeChangeCallback): void
```

取消监听当前面板大小变化，使用callback异步回调。

**起始版本：** 12

<!--Device-Panel-off(type: 'sizeChange', callback?: SizeChangeCallback): void--><!--Device-Panel-off(type: 'sizeChange', callback?: SizeChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sizeChange' | 是 |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 否 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## onHide

```TypeScript
onHide(callback: Callback<void>): void
```

监听当前面板隐藏状态，使用callback异步回调。 &lt;p&gt;“hide”事件在面板隐藏时触发。&lt;/p&gt;

**起始版本：** 23

<!--Device-Panel-onHide(callback: Callback<void>): void--><!--Device-Panel-onHide(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## onShow

```TypeScript
onShow(callback: Callback<void>): void
```

监听当前面板显示状态，使用callback异步回调。 &lt;p&gt;“show”事件在面板显示时触发。&lt;/p&gt;

**起始版本：** 23

<!--Device-Panel-onShow(callback: Callback<void>): void--><!--Device-Panel-onShow(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

## onSizeChange

```TypeScript
onSizeChange(callback: SizeChangeCallback): void
```

监听当前面板大小变化，使用callback异步回调。 &lt;p&gt;此接口仅支持固定或悬浮态的软键盘类型Panel。&lt;/p&gt;

**起始版本：** 23

<!--Device-Panel-onSizeChange(callback: SizeChangeCallback): void--><!--Device-Panel-onSizeChange(callback: SizeChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 是 |

## on_hide

```TypeScript
on(type: 'hide', callback: () => void): void
```

监听当前面板隐藏状态，使用callback异步回调。

**起始版本：** 10

<!--Device-Panel-on(type: 'hide', callback: () => void): void--><!--Device-Panel-on(type: 'hide', callback: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hide' | 是 |
| callback | () = & gt; void | 是 |

**示例**

```TypeScript
panel.on('hide', () => {
  console.info('Panel is hiding.');
});
```

## on_show

```TypeScript
on(type: 'show', callback: () => void): void
```

监听当前面板显示状态，使用 callback 异步回调。

**起始版本：** 10

<!--Device-Panel-on(type: 'show', callback: () => void): void--><!--Device-Panel-on(type: 'show', callback: () => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'show' | 是 |
| callback | () = & gt; void | 是 |

**示例**

```TypeScript
panel.on('show', () => {
  console.info('Panel is showing.');
});
```

## on_sizeChange

```TypeScript
on(type: 'sizeChange', callback: SizeChangeCallback): void
```

监听当前面板大小变化，使用callback异步回调。

**起始版本：** 12

<!--Device-Panel-on(type: 'sizeChange', callback: SizeChangeCallback): void--><!--Device-Panel-on(type: 'sizeChange', callback: SizeChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sizeChange' | 是 |
| callback | [SizeChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-sizechangecallback-t.md) | 是 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

// 监听面板大小变化事件
panel.on('sizeChange', (windowSize: window.Size) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});

// 监听面板大小变化事件（带键盘区域参数）
panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

## resize

```TypeScript
resize(width: number, height: number, callback: AsyncCallback<void>): void
```

改变当前输入法面板的大小，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-resize(width: long, height: long, callback: AsyncCallback<void>): void--><!--Device-Panel-resize(width: long, height: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 改变输入法面板大小
panel.resize(500, 1000, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in changing the panel size.');
});
```

## resize

```TypeScript
resize(width: number, height: number): Promise<void>
```

改变当前输入法面板的大小，使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-resize(width: long, height: long): Promise<void>--><!--Device-Panel-resize(width: long, height: long): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 改变输入法面板大小
panel.resize(500, 1000).then(() => {
  console.info('Succeeded in changing the panel size.');
}).catch((err: BusinessError) => {
  console.error(`Failed to resize panel. Code is ${err.code}, message is ${err.message}`);
});
```

## setImmersiveEffect

```TypeScript
setImmersiveEffect(effect: ImmersiveEffect): void
```

设置输入法应用的沉浸效果。 - 只有在[启用沉浸式模式](#setimmersivemode)时，才能使用渐变模式和流光模式。 - 只有在启用渐变模式时，才能使用流光模式。 - 未启用渐变模式时，渐变高度必须为0px。 - 只有系统应用才能设置流光模式。 - 必须先调用以下任一接口，才能调用当前接口： - [adjustPanelRect](#adjustpanelrect)(支持API version 12) - [adjustPanelRect](#adjustpanelrect)(支持 API version 15) - [resize](#resize)(支持API version 10)

**起始版本：** 23

<!--Device-Panel-setImmersiveEffect(effect: ImmersiveEffect): void--><!--Device-Panel-setImmersiveEffect(effect: ImmersiveEffect): void-End-->

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
| [12800021](../errorcode-inputmethod-framework.md#12800021-调用顺序错误) |
| [12800020](../errorcode-inputmethod-framework.md#12800020-沉浸效果参数配置错误) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
let effect: inputMethodEngine.ImmersiveEffect = {
  gradientHeight: 100,
  gradientMode: inputMethodEngine.GradientMode.LINEAR_GRADIENT
}
panel.setImmersiveEffect(effect);
```

## setImmersiveMode

```TypeScript
setImmersiveMode(mode: ImmersiveMode): void
```

设置输入法应用的沉浸模式。只能设置为不使用沉浸模式(NONE_IMMERSIVE)、浅色沉浸模式(LIGHT_IMMERSIVE)或深色沉浸模式(DARK_IMMERSIVE)。

**起始版本：** 23

<!--Device-Panel-setImmersiveMode(mode: ImmersiveMode): void--><!--Device-Panel-setImmersiveMode(mode: ImmersiveMode): void-End-->

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

**示例**

```TypeScript
panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT_IMMERSIVE);
```

## setKeepScreenOn

```TypeScript
setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>
```

设置屏幕常亮。使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>--><!--Device-Panel-setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.setKeepScreenOn(true).then(() => {
  console.info(`setKeepScreenOn success.`);
}).catch((error: BusinessError) => {
  console.error(`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}`);
})
```

## setPrivacyMode

```TypeScript
setPrivacyMode(isPrivacyMode: boolean): void
```

将输入法应用的面板设置为隐私模式，隐私模式不可被录屏、截屏。

**起始版本：** 23

**需要权限：** ohos.permission.PRIVACY_WINDOW

<!--Device-Panel-setPrivacyMode(isPrivacyMode: boolean): void--><!--Device-Panel-setPrivacyMode(isPrivacyMode: boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isPrivacyMode](../../apis-arkui/arkts-apis/arkts-arkui-window-windowproperties-i.md) | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
let isPrivacyMode: boolean = true;
panel.setPrivacyMode(isPrivacyMode);
```

## setSystemPanelButtonColor

```TypeScript
setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>
```

设置当前面板功能键颜色和功能键的背景颜色。使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>--><!--Device-Panel-setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 确保有panel实例，可以使用inputMethodEngine.getInputMethodAbility().createPanel(...)创建panel实例
try {
  let fillColor = "#FFFF00";
  let backgroundColor = "#0000FF";
  panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
    console.info(`setSystemPanelButtonColor success.`);
  }).catch((error: BusinessError) => {
    console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
  })
} catch (err) {
  let error = err as BusinessError;
  console.error(`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}`);
}
```

## setUiContent

```TypeScript
setUiContent(path: string, callback: AsyncCallback<void>): void
```

为当前的输入法面板加载具体页面内容，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-setUiContent(path: string, callback: AsyncCallback<void>): void--><!--Device-Panel-setUiContent(path: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置输入法面板内容
// panel对象通过createPanel接口获取，详见createPanel示例
panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

## setUiContent

```TypeScript
setUiContent(path: string): Promise<void>
```

为当前的输入法面板加载具体页面内容，使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-setUiContent(path: string): Promise<void>--><!--Device-Panel-setUiContent(path: string): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2').then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void
```

为当前的输入法面板加载与LocalStorage相关联的具体页面内容，使用callback异步回调。

**起始版本：** 23

<!--Device-Panel-setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void--><!--Device-Panel-setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| storage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 创建并初始化LocalStorage对象
let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in setting the content.');
});
```

## setUiContent

```TypeScript
setUiContent(path: string, storage: LocalStorage): Promise<void>
```

为当前面板加载与LocalStorage相关联的具体页面内容，使用Promise异步回调。

**起始版本：** 23

<!--Device-Panel-setUiContent(path: string, storage: LocalStorage): Promise<void>--><!--Device-Panel-setUiContent(path: string, storage: LocalStorage): Promise<void>-End-->

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 创建并初始化LocalStorage对象
let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage).then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setUiContent. Code is ${err.code}, message is ${err.message}`);
});
```

## show

```TypeScript
show(callback: AsyncCallback<void>): void
```

显示当前输入法面板，使用callback异步回调。输入法应用与编辑框绑定成功后可正常调用。

**起始版本：** 23

<!--Device-Panel-show(callback: AsyncCallback<void>): void--><!--Device-Panel-show(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.show((err: BusinessError) => {
  if (err) {
    console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the panel.');
});
```

## show

```TypeScript
show(): Promise<void>
```

显示当前输入法面板，使用promise异步回调。输入法应用与编辑框绑定成功后可正常调用。

**起始版本：** 23

<!--Device-Panel-show(): Promise<void>--><!--Device-Panel-show(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

panel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show panel. Code is ${err.code}, message is ${err.message}`);
});
```

## startMoving

```TypeScript
startMoving(): void
```

发送移动命令给窗口，不产生实际移动效果（仅在鼠标点击作用才可以移动）。

**起始版本：** 23

<!--Device-Panel-startMoving(): void--><!--Device-Panel-startMoving(): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**错误码：**

| 错误码ID |
| --- |
| [12800002](../errorcode-inputmethod-framework.md#12800002-输入法应用异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
panel.startMoving();
```

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>
```

预设置输入法应用横竖屏大小。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>--><!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>-End-->

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

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

// 目标面板状态类型
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.updatePanelRect(panelFlag, panelRect);
```

## updatePanelRect

```TypeScript
updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>--><!--Device-Panel-updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>-End-->

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
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];
// 目标面板状态类型。
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.updatePanelRect(panelFlag, panelRect);
```

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void
```

预设置输入法应用横竖屏大小。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void--><!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void-End-->

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

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

// 目标面板状态类型
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的横坐标，纵坐标，宽度以及高度
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.updatePanelRectSync(panelFlag, panelRect);
```

## updatePanelRectSync

```TypeScript
updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void
```

预设置输入法应用横竖屏大小、位置、自定义避让区域以及热区。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void--><!--Device-Panel-updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | [PanelFlag](arkts-ime-inputmethodengine-panelflag-e.md) | 是 |
| rect | [EnhancedPanelRect](arkts-ime-inputmethodengine-enhancedpanelrect-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = [landscapeRect1];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = [portraitRect1];
// 目标面板状态类型。
let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG_FIXED;
// 目标面板横屏状态及竖屏状态的位置、大小、避让区域以及热区。
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.updatePanelRectSync(panelFlag, panelRect);
```

## updateRegion

```TypeScript
updateRegion(inputRegion: Array<window.Rect>): void
```

更新当前状态下输入法面板内的热区。

**起始版本：** 23

<!--Device-Panel-updateRegion(inputRegion: Array<window.Rect>): void--><!--Device-Panel-updateRegion(inputRegion: Array<window.Rect>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputRegion | Array & lt;window.Rect & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let inputRegion: Array<window.Rect> = [{
  left: 300,
  top: 650,
  width: 2000,
  height: 500
}];
panel.updateRegion(inputRegion);
```
