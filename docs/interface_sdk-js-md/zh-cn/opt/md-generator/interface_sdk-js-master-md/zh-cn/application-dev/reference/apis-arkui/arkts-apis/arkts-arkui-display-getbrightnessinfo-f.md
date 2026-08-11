# getBrightnessInfo

## getBrightnessInfo

```TypeScript
function getBrightnessInfo(displayId: number): BrightnessInfo
```

获取指定displayId对应屏幕的亮度信息。如果屏幕不支持HDR，返回的[BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)对象中的currentHeadroom和maxHeadroom为默认值。虚拟屏的BrightnessInfo对象中sdrNits为默认值。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo--><!--Device-display-function getBrightnessInfo(displayId: long): BrightnessInfo-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
try {
  let brightnessInfo = display.getBrightnessInfo(0);
  console.info(`brightness info: ${JSON.stringify(brightnessInfo)}`);
} catch (error) {
  console.error(`Failed to getDisplayBrightness. Code: ${error.code}, message: ${error.message}`);
}
```
