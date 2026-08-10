# HttpInterceptor

Defines an HTTP Interceptor. User can implement this interface to define the handle function.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

<!--Device-http-export interface HttpInterceptor--><!--Device-http-export interface HttpInterceptor-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## interceptorHandle

```TypeScript
interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>
```

Intercept an HTTP process and do changes as disired.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-HttpInterceptor-interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>--><!--Device-HttpInterceptor-interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reqContext | [HttpRequestContext](arkts-network-http-httprequestcontext-i.md) | 是 | the context of the target HTTP request. |
| rspContext | [HttpResponse](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-httpresponse-i.md) | 是 | the context of the target HTTP response. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ChainContinue&gt; | Continue the HTTP process or terminate then return the HTTP response. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

// 创建自定义拦截器
class CustomInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // 在初始请求阶段添加认证头
    reqContext.header['Authorization'] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // 继续处理拦截器链
  }
}

let customInterceptor = new CustomInterceptor();
```

## interceptorType

```TypeScript
interceptorType: InterceptorType
```

The type of this interceptor. It defines when this intercptor would be called.

**类型：** [InterceptorType](arkts-network-http-interceptortype-e.md)

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为26.0.0。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-HttpInterceptor-interceptorType: InterceptorType--><!--Device-HttpInterceptor-interceptorType: InterceptorType-End-->

**系统能力：** SystemCapability.Communication.NetStack

