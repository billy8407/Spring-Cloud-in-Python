# -*- coding: utf-8 -*-

__author__ = "Waterball (johnny850807@gmail.com)"
__license__ = "Apache 2.0"

# standard library
from abc import ABC, abstractmethod
from urllib.parse import urlparse


class ServiceInstance(ABC):
    """
    A service's instance that owns basic HTTP info.
    """

    @property
    @abstractmethod
    def instance_id(self) -> str:
        pass

    @property
    @abstractmethod
    def service_id(self) -> str:
        pass

    @property
    @abstractmethod
    def host(self) -> str:
        pass

    @property
    @abstractmethod
    def port(self) -> int:
        pass

    @property
    @abstractmethod
    def secure(self) -> bool:
        pass

    @property
    @abstractmethod
    def uri(self) -> str:
        pass

    @property
    @abstractmethod
    def scheme(self) -> str:
        pass

    def __eq__(self, o):
        if isinstance(o, ServiceInstance):
            return (
                self.uri == o.uri
                and self.service_id == o.service_id
                and self.instance_id == o.instance_id
                and self.host == o.host
                and self.port == o.port
                and self.secure == o.secure
                and self.scheme == o.scheme
            )

        return False


class StaticServiceInstance(ServiceInstance):
    """
    A service instance that is initialized with its basic properties
    """

    def __init__(self, uri: str, service_id: str, instance_id: str):
        """
        :param uri: the url in the string type
        """
        url_obj = urlparse(uri)
        self._uri = uri
        self._scheme = url_obj.scheme
        self._secure = self._scheme == "https"
        self._host = url_obj.netloc
        self._port = url_obj.port
        self._service_id = service_id
        self._instance_id = instance_id

    @property
    def service_id(self) -> str:
        return self._service_id

    @property
    def instance_id(self) -> str:
        return self._instance_id

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def secure(self) -> bool:
        return self._secure

    @property
    def uri(self) -> str:
        return self._uri

    @property
    def scheme(self) -> str:
        return self._scheme
