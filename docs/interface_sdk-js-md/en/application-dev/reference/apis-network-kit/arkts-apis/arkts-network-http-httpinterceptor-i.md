# HttpInterceptor

Defines an HTTP Interceptor. User can implement this interface to define the handle function.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

<!--Device-http-export interface HttpInterceptor--><!--Device-http-export interface HttpInterceptor-End-->

**System capability:** SystemCapability.Communication.NetStack

## interceptorHandle

```TypeScript
interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>
```

Intercept an HTTP process and do changes as disired.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptor-interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>--><!--Device-HttpInterceptor-interceptorHandle(reqContext: HttpRequestContext, rspContext: HttpResponse): Promise<ChainContinue>-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reqContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the context of the target HTTP request. |
| rspContext | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the context of the target HTTP response. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ChainContinue&gt; | Continue the HTTP process or terminate then return the HTTP response. |

**Example**

```TypeScript
import { http } from '@kit.NetworkKit';

// Create a custom interceptor.
class CustomInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header['Authorization'] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

let customInterceptor = new CustomInterceptor();
```

```TypeScript
import { http } from '@kit.NetworkKit';

// Create a custom interceptor.
class CustomInterceptor implements http.HttpInterceptor {
  interceptorType: http.InterceptorType = http.InterceptorType.INITIAL_REQUEST;

  async interceptorHandle(reqContext: http.HttpRequestContext, rspContext: http.HttpResponse): Promise<http.ChainContinue> {
    // Add the authentication header in the initial request phase.
    reqContext.header['Authorization'] = 'Bearer token';
    console.info('Interceptor: Added authorization header');
    return true; // Continue to process the interceptor chain.
  }
}

let customInterceptor = new CustomInterceptor();
```

## interceptorType

```TypeScript
interceptorType: InterceptorType
```

The type of this interceptor. It defines when this intercptor would be called.

**Type:** InterceptorType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-HttpInterceptor-interceptorType: InterceptorType--><!--Device-HttpInterceptor-interceptorType: InterceptorType-End-->

**System capability:** SystemCapability.Communication.NetStack

