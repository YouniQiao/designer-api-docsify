# setValue（系统接口）

## setValue

```TypeScript
function setValue(value: number): void
```

设置系统的屏幕亮度。

**起始版本：** 23

**废弃版本：** -1

<!--Device-brightness-function setValue(value: int): void--><!--Device-brightness-function setValue(value: int): void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4700101](../../apis-basic-services-kit/errorcode-brightness.md#4700101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
try {
    brightness.setValue(128);
} catch (err) {
    console.error(`Failed to set brightness. Code: ${err.code}, message: ${err.message}`);
}
```


## setValue

```TypeScript
function setValue(value: number, continuous: boolean): void
```

设置系统的屏幕亮度。用于连续调节亮度的场景，在连续调节亮度过程中，设置continuous为true，结束时设置continuous为false，会有更好的性能。

**起始版本：** 23

**废弃版本：** -1

<!--Device-brightness-function setValue(value: int, continuous: boolean): void--><!--Device-brightness-function setValue(value: int, continuous: boolean): void-End-->

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |
| continuous | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4700101](../../apis-basic-services-kit/errorcode-brightness.md#4700101-连接服务失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
try {
    brightness.setValue(128, true);
} catch (err) {
    console.error(`Failed to set brightness. Code: ${err.code}, message: ${err.message}`);
}
```
