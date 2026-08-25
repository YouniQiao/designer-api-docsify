# HttpInterceptor

HTTP拦截器接口。用户可以实现此接口来定义拦截处理函数。

**起始版本：** 22

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## interceptorHandle

```TypeScript
interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>
```

拦截HTTP处理过程并进行所需的更改。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| reqContext | [HttpRequestContext](arkts-network-http-httprequestcontext-i.md) | 是 |
| rspContext | [HttpResponse](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-httpresponse-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ChainContinue](arkts-network-http-chaincontinue-t.md)&gt; |

## interceptorType

```TypeScript
interceptorType: InterceptorType
```

The type of this interceptor. It defines when this intercptor would be called.

**类型：** [InterceptorType](arkts-network-http-interceptortype-e.md)

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack
