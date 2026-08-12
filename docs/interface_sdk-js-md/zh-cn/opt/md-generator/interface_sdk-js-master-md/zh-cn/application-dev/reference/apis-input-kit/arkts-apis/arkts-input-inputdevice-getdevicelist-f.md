# getDeviceList

## getDeviceList

```TypeScript
function getDeviceList(callback: AsyncCallback<Array<number>>): void
```

获取所有输入设备的ID列表，使用callback异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void--><!--Device-inputDevice-function getDeviceList(callback: AsyncCallback<Array<int>>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 获取输入设备列表
            inputDevice.getDeviceList((error: BusinessError, ids: Array<number>) => {
              if (error) {
                console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        });
    }
  }
}
```


## getDeviceList

```TypeScript
function getDeviceList(): Promise<Array<number>>
```

获取所有输入设备的ID列表，使用Promise异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>--><!--Device-inputDevice-function getDeviceList(): Promise<Array<int>>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

## 示例

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 获取输入设备列表
            inputDevice.getDeviceList().then((ids: Array<number>) => {
              console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
