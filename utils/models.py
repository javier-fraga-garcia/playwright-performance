from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class PerformanceAudit(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    url: str = Field(alias='name')
    duration: float
    render_blocking_status: str = Field(alias='renderBlockingStatus')
    connect_start: float = Field(alias='connectStart')
    connect_end: float = Field(alias='connectEnd')
    fetch_start: float = Field(alias='fetchStart')
    request_start: float = Field(alias='requestStart')
    response_start: float = Field(alias='responseStart')
    response_end: float = Field(alias='responseEnd')
    encoded_body_size: float = Field(alias='encodedBodySize')
    decoded_body_size: float = Field(alias='decodedBodySize')
    response_status: int = Field(alias='responseStatus')
    dom_interactive: float = Field(alias='domInteractive')
    dom_content_loaded_event_start: float = Field(alias='domContentLoadedEventStart')
    dom_content_loaded_event_end: float = Field(alias='domContentLoadedEventEnd')
    dom_complete: float = Field(alias='domComplete')
    domain_lookup_start: float = Field(alias='domainLookupStart')
    domain_lookup_end: float = Field(alias='domainLookupEnd')
    load_event_start: float = Field(alias='loadEventStart')
    load_event_end: float = Field(alias='loadEventEnd')
    redirect_count: float = Field(alias='redirectCount')
    redirect_start: float = Field(alias='redirectStart')
    redirect_end: float = Field(alias='redirectEnd')
    protocol: str = Field(alias='nextHopProtocol')
    block: bool = Field(default=False)
    dt: datetime = Field(default_factory=lambda: datetime.now())
