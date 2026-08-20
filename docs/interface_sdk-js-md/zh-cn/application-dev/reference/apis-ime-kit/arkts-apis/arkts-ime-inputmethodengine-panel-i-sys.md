# Panel

**起始版本：** 23

<!--Device-inputMethodEngine-interface Panel--><!--Device-inputMethodEngine-interface Panel-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## offSizeUpdate

```TypeScript
offSizeUpdate(callback?: SizeUpdateCallback): void
```

**起始版本：** 23

<!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void--><!--Device-Panel-offSizeUpdate(callback?: SizeUpdateCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | 否 | 可选参数，需取消的目标回调函数：传入指定回调函数实例时，仅取消该回调的订阅；不传入时，取消所有sizeUpdate事件的订阅。 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

panel.offSizeUpdate((windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## off('sizeUpdate')

```TypeScript
off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void
```

**起始版本：** 14

<!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void--><!--Device-Panel-off(type: 'sizeUpdate', callback?: SizeUpdateCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | 是 | 取消监听当前面板的大小是否产生变化，固定值为'sizeUpdate'。 |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | 否 | 回调函数。用于指定要取消监听的回调函数，如果不填则取消所有sizeUpdate监听。 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

// 取消监听面板大小变化
panel.off('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  // 打印面板宽度、高度信息
  console.info(`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}`);
});
```

## onSizeUpdate

```TypeScript
onSizeUpdate(callback: SizeUpdateCallback): void
```

**起始版本：** 23

<!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void--><!--Device-Panel-onSizeUpdate(callback: SizeUpdateCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | 是 | 面板尺寸更新时触发的回调函数，入参为面板尺寸信息对象。 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

panel.onSizeUpdate((windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(`panel size changed, windowSize: ${windowSize}, keyboardArea: ${keyboardArea}`);
});
```

## on('sizeUpdate')

```TypeScript
on(type: 'sizeUpdate', callback: SizeUpdateCallback): void
```

**起始版本：** 14

<!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void--><!--Device-Panel-on(type: 'sizeUpdate', callback: SizeUpdateCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'sizeUpdate' | 是 | 监听当前面板的大小是否产生变化，固定取值为'sizeUpdate'。 |
| callback | [SizeUpdateCallback](arkts-ime-inputmethodengine-sizeupdatecallback-t-sys.md) | 是 | 面板大小变化时的回调，参数包含当前软键盘面板的宽度和高度。 |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';

// 监听面板大小变化
panel.on('sizeUpdate', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  // 打印面板大小和键盘区域信息
  console.info(`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, ` +
    `keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}`);
});
```

## setShadow

```TypeScript
setShadow(radius: double, color: string, offsetX: double, offsetY: double): void
```

**起始版本：** 23

<!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void--><!--Device-Panel-setShadow(radius: double, color: string, offsetX: double, offsetY: double): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | double | 是 | 窗口边缘阴影的模糊半径，单位px，取值范围[0.0, +∞)，0.0时关闭窗口边缘阴影。 |
| color | string | 是 | 窗口边缘阴影的颜色，十六进制RGB或ARGB格式，不区分大小写，例如`#000000`或`#FF000000`。 |
| offsetX | double | 是 | 窗口边缘阴影X轴的偏移量，单位px。正值向右偏移，负值向左偏移。 |
| offsetY | double | 是 | 窗口边缘阴影Y轴的偏移量，单位px。正值向下偏移，负值向上偏移。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [12800017](../errorcode-inputmethod-framework.md#12800017-无效的面板类型或面板状态) | invalid panel type or panel flag. Possible causes: Panel's flag is FLG_FIXED. |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | not system application. |
| [12800013](../errorcode-inputmethod-framework.md#12800013-窗口管理服务错误) | window manager service error. |

