# getDLPGatheringPolicy（系统接口）

## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(): Promise<GatheringPolicyType>
```

查询DLP沙箱聚合策略。使用Promise异步回调。

应用需要获取当前系统的DLP沙箱聚合策略配置时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>--><!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPGatheringPolicy().then((gatheringPolicy: dlpPermission.GatheringPolicyType) => {
  console.info('gatheringPolicy: ', JSON.stringify(gatheringPolicy));
}).catch((error: BusinessError)=> {
  console.error(error.message);
}); // 获取沙箱聚合策略。
```


## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void
```

查询DLP沙箱聚合策略。使用callback异步回调。

应用需要获取当前系统的DLP沙箱聚合策略配置时使用此接口。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void--><!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void-End-->

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [19100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100001-入参错误) |
| [19100011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19100011-系统服务工作异常) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPGatheringPolicy((err, gatheringPolicy) => {
  if (err) {
    console.error('getDLPGatheringPolicy error,', err.code, err.message);
  } else {
    console.info('gatheringPolicy：', JSON.stringify(gatheringPolicy));
  }
}); // 获取沙箱聚合策略。
```
