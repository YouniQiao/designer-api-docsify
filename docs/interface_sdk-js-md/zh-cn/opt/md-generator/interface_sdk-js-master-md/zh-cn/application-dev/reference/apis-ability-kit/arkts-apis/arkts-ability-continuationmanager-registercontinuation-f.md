# registerContinuation

## registerContinuation

```TypeScript
function registerContinuation(callback: AsyncCallback<number>): void
```

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-continuationManager-function registerContinuation(callback: AsyncCallback<number>): void--><!--Device-continuationManager-function registerContinuation(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600003](../errorcode-DistributedSchedule.md#16600003-应用注册token已达到最大次数限制) |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation((err, data) => {
    if (err.code != 0) {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('registerContinuation finished, ' + JSON.stringify(data));
    token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```


## registerContinuation

```TypeScript
function registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void
```

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-continuationManager-function registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void--><!--Device-continuationManager-function registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600003](../errorcode-DistributedSchedule.md#16600003-应用注册token已达到最大次数限制) |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    },
    (err, data) => {
      if (err.code != 0) {
        console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```


## registerContinuation

```TypeScript
function registerContinuation(options?: ContinuationExtraParams): Promise<number>
```

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-continuationManager-function registerContinuation(options?: ContinuationExtraParams): Promise<number>--><!--Device-continuationManager-function registerContinuation(options?: ContinuationExtraParams): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600003](../errorcode-DistributedSchedule.md#16600003-应用注册token已达到最大次数限制) |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    }).then((data) => {
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
    }).catch((err: BusinessError) => {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```
