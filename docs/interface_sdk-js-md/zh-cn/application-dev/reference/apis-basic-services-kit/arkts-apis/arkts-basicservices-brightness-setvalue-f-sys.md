# setValue（系统接口）

## 导入模块

```TypeScript
import { brightness } from '@kit.BasicServicesKit';
```

## setValue

```TypeScript
function setValue(value: int): void
```

设置系统的屏幕亮度。适用于需要固定屏幕亮度的场景，例如阅读应用、视频播放应用、夜间模式等。若需要连续调节亮度，建议使用setValue(value: number, continuous: boolean)接口。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4700101](../errorcode-brightness.md#4700101-连接服务失败) |

**示例**

```TypeScript
try {
    brightness.setValue(128);
} catch(err) {
    console.error('set brightness failed, err: ' + err);
}
```

```TypeScript
try {
    brightness.setValue(128, true);
} catch(err) {
    console.error('set brightness failed, err: ' + err);
}
```


## setValue

```TypeScript
function setValue(value: int, continuous: boolean): void
```

设置系统的屏幕亮度。用于连续调节亮度的场景，在连续调节亮度过程中，设置continuous为true，结束时设置continuous为false，会有更好的性能。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.DisplayPowerManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| continuous | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [4700101](../errorcode-brightness.md#4700101-连接服务失败) |

**示例**

参见 [setValue](#setvalue)
