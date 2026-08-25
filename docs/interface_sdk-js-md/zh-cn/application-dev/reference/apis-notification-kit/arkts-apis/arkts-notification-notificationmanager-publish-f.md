# publish

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

发布通知。使用callback异步回调。发布通知后，通知将以通知卡片的形式展示在设备的通知中心、状态栏等位置。 如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知，实现通知的更新效果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.Notification

**参见：**

isNotificationEnabled 获取指定应用的通知使能状态。

cancel 根据通知ID和标签label取消已发布的通知。

cancelAll 取消当前应用所有已发布的通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600004](../errorcode-notification.md#1600004-通知开关关闭) |
| [1600005](../errorcode-notification.md#1600005-通知渠道关闭) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
| [1600009](../errorcode-notification.md#1600009-通知发布频度超过限制) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600014](../errorcode-notification.md#1600014-没有相关权限) |
| [1600015](../errorcode-notification.md#1600015-当前通知状态不支持重复配置) |
| [1600016](../errorcode-notification.md#1600016-本次更新的通知版本太低) |
| [1600020](../errorcode-notification.md#1600020-不允许权限管控名单中的应用发布通知) |
| [1600029](../errorcode-notification.md#1600029-系统无法找到实况窗卡片自定义扩展区的extensionability) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-无法连接到服务器) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in publishing notification.`);
  }
}
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'test_title',
      text: 'test_text',
      additionalText: 'test_additionalText'
    }
  }
};
notificationManager.publish(notificationRequest, publishCallback);
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError | null): void => {
  if (err) {
    console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in publishing notification.`);
  }
}
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'test_title',
      text: 'test_text',
      additionalText: 'test_additionalText'
    }
  }
};
notificationManager.publish(notificationRequest, publishCallback);
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'test_title',
      text: 'test_text',
      additionalText: 'test_additionalText'
    }
  }
};
notificationManager.publish(notificationRequest).then(() => {
  console.info(`Succeeded in publishing notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'test_title',
      text: 'test_text',
      additionalText: 'test_additionalText'
    }
  }
};
notificationManager.publish(notificationRequest).then(() => {
  console.info(`Succeeded in publishing notification.`);
}).catch((err: Error): void => {
  let error: BusinessError = err as BusinessError;
  console.error(`Failed to publish notification. Code is ${error.code}, message is ${error.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('publish success');
    }
}
// 用户ID，使用时需替换为真实的userId。
let userId: number = 1;
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
        }
    }
};
notificationManager.publish(notificationRequest, userId, publishCallback);
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError | null) => {
    if (err) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('publish success');
    }
}
// 用户ID，使用时需替换为真实的userId。
let userId: int = 1;
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
        }
    }
};
notificationManager.publish(notificationRequest, userId, publishCallback);
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
        }
    }
};

// 用户ID，使用时需替换为真实的userId。
let userId: number = 1;

notificationManager.publish(notificationRequest, userId).then(() => {
    console.info('publish success');
}).catch((err: BusinessError) => {
    console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
        }
    }
};

// 用户ID，使用时需替换为真实的userId。
let userId: int = 1;

notificationManager.publish(notificationRequest, userId).then(() => {
    console.info('publish success');
}).catch((err: Error): void => {
    let error: BusinessError = err as BusinessError;
    console.error(`publish failed, code is ${error.code}, message is ${error.message}`);
});
```


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

发布通知。使用Promise异步回调。发布通知后，通知将以通知卡片的形式展示在设备的通知中心、状态栏等位置。 如果新发布通知与已发布通知的ID和标签都相同，则新通知将取代原有通知，实现通知的更新效果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Notification.Notification

**参见：**

isNotificationEnabled 查询当前应用通知授权状态。

cancel 根据通知ID和标签label取消已发布的通知。

cancelAll 取消当前应用所有已发布的通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600004](../errorcode-notification.md#1600004-通知开关关闭) |
| [1600005](../errorcode-notification.md#1600005-通知渠道关闭) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
| [1600009](../errorcode-notification.md#1600009-通知发布频度超过限制) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600014](../errorcode-notification.md#1600014-没有相关权限) |
| [1600015](../errorcode-notification.md#1600015-当前通知状态不支持重复配置) |
| [1600016](../errorcode-notification.md#1600016-本次更新的通知版本太低) |
| [1600020](../errorcode-notification.md#1600020-不允许权限管控名单中的应用发布通知) |
| [1600029](../errorcode-notification.md#1600029-系统无法找到实况窗卡片自定义扩展区的extensionability) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-无法连接到服务器) |

**示例**

参见 [publish](#publish)
