from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import FlightSerializer, AirlineSerializer, EmployeeSerializer, GateSerializer, BaggageSerializer, CreateFlightSerializer, CreateGateSerializer, CreateEmployeeSerializer, CreateBaggageSerializer, CreateAirlineSerializer, UpdateAirlineSerializer, UpdateFlightSerializer, UpdateGateSerializer, UpdateEmployeeSerializer,UpdateBaggageSerializer
from .models import Flight, Airline, Employee, Gate, Baggage

# Create your views here.

class FlightView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class CreateFlightView(APIView):
    serializer_class = CreateFlightSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            flightCode = serializer.data.get('flightCode')
            flightSource = serializer.data.get('flightSource')
            flightDestination = serializer.data.get('flightDestination')
            flightArrival = serializer.data.get('flightArrival')
            flightDeparture = serializer.data.get('flightDeparture')
            flightStatus = serializer.data.get('flightStatus')
            flightType = serializer.data.get('flightType')
            flightNoOfStops = serializer.data.get('flightNoOfStops')
            flightGate = serializer.data.get('flightGate')
            flightCarouselNo = serializer.data.get('flightCarouselNo')
                    
            flight = Flight(flightCode=flightCode, flightSource=flightSource, flightDestination=flightDestination, flightArrival=flightArrival, flightDeparture=flightDeparture, flightStatus=flightStatus, flightType=flightType, flightNoOfStops=flightNoOfStops, flightGate=flightGate, flightCarouselNo=flightCarouselNo)
            flight.save()

            return Response(FlightSerializer(flight).data, status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetFlightView(APIView):
    serializer_class = FlightSerializer
    lookup_url_kwarg = 'flightCode'
    def get(self, request, format=None):

        flightCode = request.GET.get(self.lookup_url_kwarg)
        if flightCode != None:
            flight = Flight.objects.filter(flightCode=flightCode)
            if (len(flight) > 0):
                data = FlightSerializer(flight[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response('Flight not found: Invalid flight code', status=status.HTTP_404_NOT_FOUND)

        return Response('Bad request: Flight code parameter not found in request', status=status.HTTP_400_BAD_REQUEST)

class UpdateFlightView(APIView):
    serializer_class = UpdateFlightSerializer

    def patch(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            flightCode = serializer.data.get('flightCode')
            flightSource = serializer.data.get('flightSource')
            flightDestination = serializer.data.get('flightDestination')
            flightArrival = serializer.data.get('flightArrival')
            flightDeparture = serializer.data.get('flightDeparture')
            flightStatus = serializer.data.get('flightStatus')
            flightType = serializer.data.get('flightType')
            flightNoOfStops = serializer.data.get('flightNoOfStops')
            flightGate = serializer.data.get('flightGate')
            flightCarouselNo = serializer.data.get('flightCarouselNo')
                    
            queryset = Flight.objects.filter(flightCode=flightCode)
            if not queryset.exists():
                return Response({'msg':'Flight not found.'}, status=status.HTTP_404_NOT_FOUND)

            flight = queryset[0]
            # flight.flightCode = flightCode
            flight.flightSource = flightSource
            flight.flightDestination = flightDestination
            flight.flightArrival = flightArrival
            flight.flightDeparture = flightDeparture
            flight.flightStatus = flightStatus
            flight.flightType = flightType
            flight.flightNoOfStops = flightNoOfStops
            flight.flightGate = flightGate
            flight.flightCarouselNo = flightCarouselNo

            flight.save(update_fields=['flightSource', 'flightDestination','flightArrival','flightDeparture','flightStatus','flightType','flightNoOfStops', 'flightGate','flightCarouselNo'])

            return Response(FlightSerializer(flight).data, status=status.HTTP_200_OK)

        else:
            return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

class AirlineView(generics.CreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class CreateAirlineView(APIView):
    serializer_class = CreateAirlineSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            airlineID = serializer.data.get('airlineID')
            airlineName = serializer.data.get('airlineName')

            airline = Airline(airlineID = airlineID, airlineName = airlineName)
            airline.save()

            return Response(AirlineSerializer(airline).data, status=status.HTTP_201_CREATED)        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetAirlineView(APIView):
    serializer_class = AirlineSerializer
    lookup_url_kwarg = 'airlineID'
    
    def get(self, request, format=None):
        airlineID = request.GET.get(self.lookup_url_kwarg)
        if airlineID != None:
            airline = Airline.objects.filter(airlineID = airlineID)
            if (len(airline) > 0):
                data = AirlineSerializer(airline[0]).data
                return Response(data, status=status.HTTP_200_OK)
            
            return Response('Airline not found: Invalid Airline ID', status=status.HTTP_404_NOT_FOUND)

        return Response('Bad request: Airline ID parameter not found in request', status=status.HTTP_400_BAD_REQUEST)

class UpdateAirlineView(APIView):
    serializer_class = UpdateAirlineSerializer

    def patch(self, request, format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            airlineID = serializer.data.get('airlineID')
            airlineName = serializer.data.get('airlineName')

            queryset = Airline.objects.filter(airlineID=airlineID)
            if not queryset.exists():
                return Response('Airline ID does not exist', status=status.HTTP_404_NOT_FOUND)
            
            airline = queryset[0]
            airline.airlineName = airlineName
            airline.save(update_fields=['airlineName'])
            return Response(AirlineSerializer(airline).data, status=status.HTTP_200_OK)        
        else:
            return Response('Bad request: Invalid data', status=status.HTTP_400_BAD_REQUEST)

class EmployeeView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CreateEmployeeView(APIView):
    serializer_class = CreateEmployeeSerializer
    def post(self, request, Format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            employeeID = serializer.data.get('employeeID')
            employeeFirstName = serializer.data.get('employeeFirstName')
            employeeLastName = serializer.data.get('employeeLastName')
            employeeEmail = serializer.data.get('employeeEmail')
            employeeType = serializer.data.get('employeeType')
            password = serializer.data.get('password')
                    
            employee = Employee(employeeID = employeeID, employeeFirstName = employeeFirstName, employeeLastName = employeeLastName, employeeEmail = employeeEmail, employeeType = employeeType, password = password)
            employee.save()

            return Response(EmployeeSerializer(employee).data, status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetEmployeeView(APIView):
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'employeeID'
    def get(self, request, format=None):

        employeeID = request.GET.get(self.lookup_url_kwarg)
        if employeeID != None:
            employee = Employee.objects.filter(employeeID = employeeID)
            if (len(employee) > 0):
                data = EmployeeSerializer(employee[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response('Employee not found: Invalid employee ID', status=status.HTTP_404_NOT_FOUND)

        return Response('Bad request: Employee ID parameter not found in request', status=status.HTTP_400_BAD_REQUEST)

class UpdateEmployeeView(APIView):
    serializer_class = UpdateEmployeeSerializer

    def patch(self, request, format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            employeeID = serializer.data.get('employeeID')
            employeeFirstName = serializer.data.get('employeeFirstName')
            employeeLastName = serializer.data.get('employeeLastName')
            employeeEmail = serializer.data.get('employeeEmail')
            employeeType = serializer.data.get('employeeType')
            password = serializer.data.get('password')

            queryset = Employee.objects.filter(employeeID=employeeID)
            if not queryset.exists():
                return Response('Employee does not exist', status=status.HTTP_404_NOT_FOUND)
            
            employee = queryset[0]
            employee.employeeFirstName = employeeFirstName
            employee.employeeLastName = employeeLastName
            employee.employeeEmail = employeeEmail
            employee.employeeType = employeeType
            employee.password = password

            employee.save(update_fields=['employeeFirstName', 'employeeLastName', 'employeeEmail', 'employeeType', 'password'])
            return Response(EmployeeSerializer(employee).data, status=status.HTTP_200_OK)        
        else:
            # print(serializer.errors);
            return Response('Bad request: Invalid data', status=status.HTTP_400_BAD_REQUEST)

class GateView(generics.CreateAPIView):
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

class CreateGateView(APIView):
    serializer_class = CreateGateSerializer
    def post(self, request, Format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            gateNo = serializer.data.get('gateNo')
            gateStatus = serializer.data.get('gateStatus')
                    
            gate = Gate(gateNo=gateNo, gateStatus=gateStatus)
            gate.save()

            return Response(GateSerializer(gate).data, status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetGateView(APIView):
    serializer_class = GateSerializer
    lookup_url_kwarg = 'gateNo'
    def get(self, request, format=None):

        gateNo = request.GET.get(self.lookup_url_kwarg)
        if gateNo != None:
            gate = Gate.objects.filter(gateNo=gateNo)
            if (len(gate) > 0):
                data = GateSerializer(gate[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response('Gate not found: Invalid gate number', status=status.HTTP_404_NOT_FOUND)

        return Response('Bad request: Gate number parameter not found in request', status=status.HTTP_400_BAD_REQUEST)


class UpdateGateView(APIView):
    serializer_class = UpdateGateSerializer

    def patch(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            gateNo = serializer.data.get('gateNo')
            gateStatus = serializer.data.get('gateStatus')
                    
            queryset = Gate.objects.filter(gateNo=gateNo)
            if not queryset.exists():
                return Response({'msg':'Gate not found.'}, status=status.HTTP_404_NOT_FOUND)

            gate = queryset[0]
            gate.gateStatus = gateStatus

            gate.save(update_fields=['gateStatus'])

            return Response(GateSerializer(gate).data, status=status.HTTP_200_OK)

        else:
            return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class BaggageView(generics.CreateAPIView):
    queryset = Baggage.objects.all()
    serializer_class = BaggageSerializer


class CreateBaggageView(APIView):
    serializer_class = CreateBaggageSerializer
    def post(self, request, Format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            baggageCarouselNo = serializer.data.get('baggageCarouselNo')
            baggageStatus = serializer.data.get('baggageStatus')
                    
            baggage = Baggage(baggageCarouselNo=baggageCarouselNo, baggageStatus=baggageStatus)
            baggage.save()

            return Response(BaggageSerializer(baggage).data, status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetBaggageView(APIView):
    serializer_class = GateSerializer
    lookup_url_kwarg = 'baggageCarouselNo'
    def get(self, request, format=None):

        baggageCarouselNo = request.GET.get(self.lookup_url_kwarg)
        if baggageCarouselNo != None:
            baggage = Baggage.objects.filter(baggageCarouselNo=baggageCarouselNo)
            if (len(baggage) > 0):
                data = BaggageSerializer(baggage[0]).data
                return Response(data, status=status.HTTP_200_OK)

            return Response('Baggage Carousel not found: Invalid baggage carousel number', status=status.HTTP_404_NOT_FOUND)

        return Response('Bad request: Baggage Carousel number parameter not found in request', status=status.HTTP_400_BAD_REQUEST)

class UpdateBaggageView(APIView):
    serializer_class = UpdateBaggageSerializer

    def patch(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            baggageCarouselNo = serializer.data.get('baggageCarouselNo')
            baggageStatus = serializer.data.get('baggageStatus')
                    
            queryset = Baggage.objects.filter(baggageCarouselNo=baggageCarouselNo)
            if not queryset.exists():
                return Response({'msg':'Baggage Carousel not found.'}, status=status.HTTP_404_NOT_FOUND)

            baggage = queryset[0]
            baggage.baggageStatus = baggageStatus

            baggage.save(update_fields=['baggageStatus'])

            return Response(BaggageSerializer(baggage).data, status=status.HTTP_200_OK)

        else:
            return Response({'Bad request':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)