# transmitInfrared

## transmitInfrared

```TypeScript
function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void
```

产生特定频率和特定电平大小的红外信号。

**起始版本：** 15

**需要权限：** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

<!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void--><!--Device-infraredEmitter-function transmitInfrared(infraredFrequency: long, pattern: Array<long>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InfraredEmitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| infraredFrequency | number | 是 |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | Array & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { infraredEmitter } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 设置红外频率及红外电平信号模式
            infraredEmitter.transmitInfrared(38000, [100, 200, 300, 400]);
          } catch (error) {
            console.error(`Failed to transmit infrared signal, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
