# setShieldStatus（系统接口）

## setShieldStatus

```TypeScript
function setShieldStatus(shieldMode: ShieldMode, isShield: boolean): void
```

设置系统快捷键屏蔽类型。

**起始版本：** 11

**需要权限：** ohos.permission.INPUT_CONTROL_DISPATCHING

<!--Device-inputConsumer-function setShieldStatus(shieldMode: ShieldMode, isShield: boolean): void--><!--Device-inputConsumer-function setShieldStatus(shieldMode: ShieldMode, isShield: boolean): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shieldMode | [ShieldMode](arkts-input-inputconsumer-shieldmode-e-sys.md) | 是 |
| isShield | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { inputConsumer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let FACTORY_MODE = 0;
          try {
            // 设置屏蔽状态
            inputConsumer.setShieldStatus(FACTORY_MODE, true);
            console.info(`Succeeded in setting shield status.`);
          } catch (error) {
            console.error(`Failed to set shield status, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
