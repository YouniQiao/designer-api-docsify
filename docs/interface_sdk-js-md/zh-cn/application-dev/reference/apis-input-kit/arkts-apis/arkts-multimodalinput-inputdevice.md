# @ohos.multimodalInput.inputDevice(输入设备)

本模块提供输入设备管理能力，包括查询输入设备信息，设置/获取键盘按键重复时延，设置输入设备的开关状态等。

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

## 导入模块

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getDevice(输入设备)](arkts-input-inputdevice-getdevice-f.md) |
| [getDevice(输入设备)](arkts-input-inputdevice-getdevice-f.md) |
| [getDeviceIds(输入设备)](arkts-input-inputdevice-getdeviceids-f.md) |
| [getDeviceIds(输入设备)](arkts-input-inputdevice-getdeviceids-f.md) |
| [getDeviceInfo(输入设备)](arkts-input-inputdevice-getdeviceinfo-f.md) |
| [getDeviceInfo(输入设备)](arkts-input-inputdevice-getdeviceinfo-f.md) |
| [getDeviceInfoSync(输入设备)](arkts-input-inputdevice-getdeviceinfosync-f.md) |
| [getDeviceList(输入设备)](arkts-input-inputdevice-getdevicelist-f.md) |
| [getDeviceList(输入设备)](arkts-input-inputdevice-getdevicelist-f.md) |
| [getIntervalSinceLastInput(输入设备)](arkts-input-inputdevice-getintervalsincelastinput-f.md) |
| [getKeyboardType(输入设备)](arkts-input-inputdevice-getkeyboardtype-f.md) |
| [getKeyboardType(输入设备)](arkts-input-inputdevice-getkeyboardtype-f.md) |
| [getKeyboardTypeSync(输入设备)](arkts-input-inputdevice-getkeyboardtypesync-f.md) |
| [isFunctionKeyEnabled(输入设备)](arkts-input-inputdevice-isfunctionkeyenabled-f.md) |
| [off(输入设备)](arkts-input-inputdevice-off-f.md#offchange) |
| [offChange(输入设备)](arkts-input-inputdevice-offchange-f.md) |
| [on(输入设备)](arkts-input-inputdevice-on-f.md#onchange) |
| [onChange(输入设备)](arkts-input-inputdevice-onchange-f.md) |
| [setFunctionKeyEnabled(输入设备)](arkts-input-inputdevice-setfunctionkeyenabled-f.md) |
| [supportKeys(输入设备)](arkts-input-inputdevice-supportkeys-f.md) |
| [supportKeys(输入设备)](arkts-input-inputdevice-supportkeys-f.md) |
| [supportKeysSync(输入设备)](arkts-input-inputdevice-supportkeyssync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [bindToDisplay(输入设备)](arkts-input-inputdevice-bindtodisplay-f-sys.md) |
| [getKeyboardRepeatDelay(输入设备)](arkts-input-inputdevice-getkeyboardrepeatdelay-f-sys.md) |
| [getKeyboardRepeatDelay(输入设备)](arkts-input-inputdevice-getkeyboardrepeatdelay-f-sys.md) |
| [getKeyboardRepeatRate(输入设备)](arkts-input-inputdevice-getkeyboardrepeatrate-f-sys.md) |
| [getKeyboardRepeatRate(输入设备)](arkts-input-inputdevice-getkeyboardrepeatrate-f-sys.md) |
| [setInputDeviceEnabled(输入设备)](arkts-input-inputdevice-setinputdeviceenabled-f-sys.md) |
| [setKeyboardRepeatDelay(输入设备)](arkts-input-inputdevice-setkeyboardrepeatdelay-f-sys.md) |
| [setKeyboardRepeatDelay(输入设备)](arkts-input-inputdevice-setkeyboardrepeatdelay-f-sys.md) |
| [setKeyboardRepeatRate(输入设备)](arkts-input-inputdevice-setkeyboardrepeatrate-f-sys.md) |
| [setKeyboardRepeatRate(输入设备)](arkts-input-inputdevice-setkeyboardrepeatrate-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AxisRange(输入设备)](arkts-input-inputdevice-axisrange-i.md) |
| [DeviceListener(输入设备)](arkts-input-inputdevice-devicelistener-i.md) |
| [InputDeviceData(输入设备)](arkts-input-inputdevice-inputdevicedata-i.md) |

### 枚举

| 名称 |
| --- |
| [FunctionKey(输入设备)](arkts-input-inputdevice-functionkey-e.md) |
| [KeyboardType(输入设备)](arkts-input-inputdevice-keyboardtype-e.md) |

### 类型

| 名称 |
| --- |
| [AxisType(输入设备)](arkts-input-inputdevice-axistype-t.md) |
| [ChangedType(输入设备)](arkts-input-inputdevice-changedtype-t.md) |
| [SourceType(输入设备)](arkts-input-inputdevice-sourcetype-t.md) |
