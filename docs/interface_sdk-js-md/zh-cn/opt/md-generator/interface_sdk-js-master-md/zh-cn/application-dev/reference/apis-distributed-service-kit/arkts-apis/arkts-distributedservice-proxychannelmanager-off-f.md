# off

## off('receiveData')

```TypeScript
function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void
```

取消订阅数据接收事件，停止接收数据。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'receiveData' | 是 |
| channelId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32390006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-参数错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [32390004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-通道id非法或者不可用) |
| [32390100](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-调用受限) |

## 示例

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          try {
            proxyChannelManager.off('receiveData', channelId); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to unregister receiveData callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```


## off('channelStateChange')

```TypeScript
function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void
```

取消订阅通道状态事件。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'channelStateChange' | 是 |
| channelId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32390006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-参数错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [32390004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-通道id非法或者不可用) |
| [32390100](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-调用受限) |

## 示例

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          try {
            proxyChannelManager.off('channelStateChange', channelId); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to unregister channelStateChange callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
