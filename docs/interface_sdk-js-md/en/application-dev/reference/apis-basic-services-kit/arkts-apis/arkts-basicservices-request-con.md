# Constants

## ERROR_CANNOT_RESUME

```TypeScript
const ERROR_CANNOT_RESUME: int
```

(Download error codes) Failure to resume the download due to network errors.

**Since:** 23

<!--Device-request-const ERROR_CANNOT_RESUME: int--><!--Device-request-const ERROR_CANNOT_RESUME: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_DEVICE_NOT_FOUND

```TypeScript
const ERROR_DEVICE_NOT_FOUND: int
```

(Download error codes) Failure to find a storage device such as a memory card.

**Since:** 23

<!--Device-request-const ERROR_DEVICE_NOT_FOUND: int--><!--Device-request-const ERROR_DEVICE_NOT_FOUND: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_FILE_ALREADY_EXISTS

```TypeScript
const ERROR_FILE_ALREADY_EXISTS: int
```

(Download error codes) Failure to download the file because it already exists.

**Since:** 23

<!--Device-request-const ERROR_FILE_ALREADY_EXISTS: int--><!--Device-request-const ERROR_FILE_ALREADY_EXISTS: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_FILE_ERROR

```TypeScript
const ERROR_FILE_ERROR: int
```

(Download error codes) File operation failed.

**Since:** 23

<!--Device-request-const ERROR_FILE_ERROR: int--><!--Device-request-const ERROR_FILE_ERROR: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_HTTP_DATA_ERROR

```TypeScript
const ERROR_HTTP_DATA_ERROR: int
```

(Download error codes) HTTP transmission failed.

**Since:** 23

<!--Device-request-const ERROR_HTTP_DATA_ERROR: int--><!--Device-request-const ERROR_HTTP_DATA_ERROR: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_INSUFFICIENT_SPACE

```TypeScript
const ERROR_INSUFFICIENT_SPACE: int
```

(Download error codes) Insufficient storage space.

**Since:** 23

<!--Device-request-const ERROR_INSUFFICIENT_SPACE: int--><!--Device-request-const ERROR_INSUFFICIENT_SPACE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_OFFLINE

```TypeScript
const ERROR_OFFLINE: int
```

(Download error codes) No network connection.

**Since:** 23

<!--Device-request-const ERROR_OFFLINE: int--><!--Device-request-const ERROR_OFFLINE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_TOO_MANY_REDIRECTS

```TypeScript
const ERROR_TOO_MANY_REDIRECTS: int
```

(Download error codes) Error caused by too many network redirections.

**Since:** 23

<!--Device-request-const ERROR_TOO_MANY_REDIRECTS: int--><!--Device-request-const ERROR_TOO_MANY_REDIRECTS: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_UNHANDLED_HTTP_CODE

```TypeScript
const ERROR_UNHANDLED_HTTP_CODE: int
```

(Download error codes) Unidentified HTTP code.

**Since:** 23

<!--Device-request-const ERROR_UNHANDLED_HTTP_CODE: int--><!--Device-request-const ERROR_UNHANDLED_HTTP_CODE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_UNKNOWN

```TypeScript
const ERROR_UNKNOWN: int
```

(Download error codes) Unknown error. In API version 12 or earlier, only serial connection to the IP addresses associated with the specified domain name is supported, and the connection time for a single IP address is not controllable. If the first IP address returned by the DNS is blocked, a handshake timeout may occur, leading to an ERROR_UNKNOWN error.

**Since:** 23

<!--Device-request-const ERROR_UNKNOWN: int--><!--Device-request-const ERROR_UNKNOWN: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## ERROR_UNSUPPORTED_NETWORK_TYPE

```TypeScript
const ERROR_UNSUPPORTED_NETWORK_TYPE: int
```

(Download error codes) Network type mismatch.

**Since:** 23

<!--Device-request-const ERROR_UNSUPPORTED_NETWORK_TYPE: int--><!--Device-request-const ERROR_UNSUPPORTED_NETWORK_TYPE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_FILEIO

```TypeScript
const EXCEPTION_FILEIO: int
```

(Specific error codes) Abnormal file operation.

**Since:** 23

<!--Device-request-const EXCEPTION_FILEIO: int--><!--Device-request-const EXCEPTION_FILEIO: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_FILEPATH

```TypeScript
const EXCEPTION_FILEPATH: int
```

(Specific error codes) Abnormal file path.

**Since:** 23

<!--Device-request-const EXCEPTION_FILEPATH: int--><!--Device-request-const EXCEPTION_FILEPATH: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_OTHERS

```TypeScript
const EXCEPTION_OTHERS: int
```

(Specific error codes) Other errors.

**Since:** 23

<!--Device-request-const EXCEPTION_OTHERS: int--><!--Device-request-const EXCEPTION_OTHERS: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_PARAMCHECK

```TypeScript
const EXCEPTION_PARAMCHECK: int
```

(Universal error codes) Parameter check failed.

**Since:** 23

<!--Device-request-const EXCEPTION_PARAMCHECK: int--><!--Device-request-const EXCEPTION_PARAMCHECK: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_PERMISSION

```TypeScript
const EXCEPTION_PERMISSION: int
```

(Universal error codes) Permission verification failed.

**Since:** 23

<!--Device-request-const EXCEPTION_PERMISSION: int--><!--Device-request-const EXCEPTION_PERMISSION: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_SERVICE

```TypeScript
const EXCEPTION_SERVICE: int
```

(Specific error codes) Abnormal service.

**Since:** 23

<!--Device-request-const EXCEPTION_SERVICE: int--><!--Device-request-const EXCEPTION_SERVICE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## EXCEPTION_UNSUPPORTED

```TypeScript
const EXCEPTION_UNSUPPORTED: int
```

(Universal error codes) The device does not support this API.

**Since:** 23

<!--Device-request-const EXCEPTION_UNSUPPORTED: int--><!--Device-request-const EXCEPTION_UNSUPPORTED: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## NETWORK_MOBILE

```TypeScript
const NETWORK_MOBILE: int
```

(Network type) Bit flag download allowed on a mobile network.

**Since:** 23

<!--Device-request-const NETWORK_MOBILE: int--><!--Device-request-const NETWORK_MOBILE: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## NETWORK_WIFI

```TypeScript
const NETWORK_WIFI: int
```

(Network type) Bit flag download allowed on a WLAN.

**Since:** 23

<!--Device-request-const NETWORK_WIFI: int--><!--Device-request-const NETWORK_WIFI: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## PAUSED_BY_USER

```TypeScript
const PAUSED_BY_USER: int
```

(Causes of download pause) The user paused the session.

**Since:** 23

<!--Device-request-const PAUSED_BY_USER: int--><!--Device-request-const PAUSED_BY_USER: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## PAUSED_QUEUED_FOR_WIFI

```TypeScript
const PAUSED_QUEUED_FOR_WIFI: int
```

(Causes of download pause) Download paused and queuing for a WLAN connection because the file size exceeds the maximum value allowed for a mobile network session.

**Since:** 23

<!--Device-request-const PAUSED_QUEUED_FOR_WIFI: int--><!--Device-request-const PAUSED_QUEUED_FOR_WIFI: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## PAUSED_UNKNOWN

```TypeScript
const PAUSED_UNKNOWN: int
```

(Causes of download pause) Download paused due to unknown reasons.

**Since:** 23

<!--Device-request-const PAUSED_UNKNOWN: int--><!--Device-request-const PAUSED_UNKNOWN: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## PAUSED_WAITING_FOR_NETWORK

```TypeScript
const PAUSED_WAITING_FOR_NETWORK: int
```

(Causes of download pause) Download paused due to a network connection problem. Example: network disconnection

**Since:** 23

<!--Device-request-const PAUSED_WAITING_FOR_NETWORK: int--><!--Device-request-const PAUSED_WAITING_FOR_NETWORK: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## PAUSED_WAITING_TO_RETRY

```TypeScript
const PAUSED_WAITING_TO_RETRY: int
```

(Causes of download pause) Download paused due to network error and then retried.

**Since:** 23

<!--Device-request-const PAUSED_WAITING_TO_RETRY: int--><!--Device-request-const PAUSED_WAITING_TO_RETRY: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## SESSION_FAILED

```TypeScript
const SESSION_FAILED: int
```

(Download task status codes) Download failure without retry.

**Since:** 23

<!--Device-request-const SESSION_FAILED: int--><!--Device-request-const SESSION_FAILED: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## SESSION_PAUSED

```TypeScript
const SESSION_PAUSED: int
```

(Download task status codes) Download paused.

**Since:** 23

<!--Device-request-const SESSION_PAUSED: int--><!--Device-request-const SESSION_PAUSED: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## SESSION_PENDING

```TypeScript
const SESSION_PENDING: int
```

(Download task status codes) Download pending.

**Since:** 23

<!--Device-request-const SESSION_PENDING: int--><!--Device-request-const SESSION_PENDING: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## SESSION_RUNNING

```TypeScript
const SESSION_RUNNING: int
```

(Download task status codes) Download in progress.

**Since:** 23

<!--Device-request-const SESSION_RUNNING: int--><!--Device-request-const SESSION_RUNNING: int-End-->

**System capability:** SystemCapability.MiscServices.Download

## SESSION_SUCCESSFUL

```TypeScript
const SESSION_SUCCESSFUL: int
```

(Download task status codes) Successful download.

**Since:** 23

<!--Device-request-const SESSION_SUCCESSFUL: int--><!--Device-request-const SESSION_SUCCESSFUL: int-End-->

**System capability:** SystemCapability.MiscServices.Download

