
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date, timedelta

engine = create_engine(
    "postgresql+psycopg2://postgres:Mokia123$@localhost:1940/hotel_db"
)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    stars = Column(Integer, nullable=False)

    rooms = relationship(
        "Room",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    room_number = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship(
        "Booking",
        back_populates="room",
        cascade="all, delete-orphan"
    )


class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    bookings = relationship(
        "Booking",
        back_populates="guest",
        cascade="all, delete-orphan"
    )


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)

    guest = relationship("Guest", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")


Base.metadata.create_all(engine)


def add_hotel(name, country, city, stars):
    hotel = Hotel(
        name=name,
        country=country,
        city=city,
        stars=stars
    )
    session.add(hotel)
    session.commit()
    return hotel


def add_room(room_number, floor, price_per_night, hotel_id):
    room = Room(
        room_number=room_number,
        floor=floor,
        price_per_night=price_per_night,
        hotel_id=hotel_id
    )
    session.add(room)
    session.commit()
    return room


def add_guest(first_name, last_name, email, phone):
    guest = Guest(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone
    )
    session.add(guest)
    session.commit()
    return guest


def create_booking(guest_id, room_id, check_in, check_out):
    booking = Booking(
        guest_id=guest_id,
        room_id=room_id,
        check_in=check_in,
        check_out=check_out
    )
    session.add(booking)
    session.commit()
    return booking


def get_all_hotels():
    return session.query(Hotel).all()


def get_hotel_by_id(hotel_id):
    return session.query(Hotel).filter(Hotel.id == hotel_id).first()


def get_all_rooms():
    return session.query(Room).all()


def get_guest_by_email(email):
    return session.query(Guest).filter(Guest.email == email).first()


def update_room_price(room_id, new_price):
    room = session.query(Room).filter(Room.id == room_id).first()

    if room:
        room.price_per_night = new_price
        session.commit()
        return True

    return False


def delete_guest(guest_id):
    guest = session.query(Guest).filter(Guest.id == guest_id).first()

    if guest:
        session.delete(guest)
        session.commit()
        return True

    return False


def delete_room(room_id):
    room = session.query(Room).filter(Room.id == room_id).first()

    if room:
        session.delete(room)
        session.commit()
        return True

    return False


if not session.query(Hotel).first():

    hotel1 = add_hotel("Grand Hotel", "Georgia", "Tbilisi", 5)
    hotel2 = add_hotel("Tbilisi Palace", "Georgia", "Tbilisi", 4)
    hotel3 = add_hotel("Batumi Hotel", "Georgia", "Batumi", 5)

    room1 = add_room(101, 1, 80, hotel1.id)
    room2 = add_room(102, 1, 120, hotel1.id)
    room3 = add_room(201, 2, 180, hotel1.id)

    room4 = add_room(101, 1, 70, hotel2.id)
    room5 = add_room(202, 2, 110, hotel2.id)
    room6 = add_room(303, 3, 150, hotel2.id)

    room7 = add_room(101, 1, 90, hotel3.id)
    room8 = add_room(202, 2, 130, hotel3.id)
    room9 = add_room(305, 3, 250, hotel3.id)

    guest1 = add_guest("Giorgi", "Beridze", "giorgi@gmail.com", "555111111")
    guest2 = add_guest("Nika", "Kapanadze", "nika@gmail.com", "555222222")
    guest3 = add_guest("Ana", "Maisuradze", "ana@gmail.com", "555333333")
    guest4 = add_guest("Luka", "Gelashvili", "luka@gmail.com", "555444444")
    guest5 = add_guest("Mari", "Japaridze", "mari@gmail.com", "555555555")

    today = date.today()

    create_booking(guest1.id, room1.id, today - timedelta(days=10), today + timedelta(days=2))
    create_booking(guest1.id, room2.id, today + timedelta(days=5), today + timedelta(days=10))
    create_booking(guest2.id, room3.id, today - timedelta(days=3), today + timedelta(days=4))
    create_booking(guest2.id, room4.id, today + timedelta(days=10), today + timedelta(days=15))
    create_booking(guest3.id, room5.id, today + timedelta(days=2), today + timedelta(days=6))
    create_booking(guest4.id, room7.id, today - timedelta(days=5), today + timedelta(days=1))
    create_booking(guest5.id, room9.id, today + timedelta(days=20), today + timedelta(days=25))


five_star_hotels = session.query(Hotel).filter(
    Hotel.stars == 5
).all()

for hotel in five_star_hotels:
    print(hotel.name)


tbilisi_hotels = session.query(Hotel).filter(
    Hotel.city == "Tbilisi"
).all()

for hotel in tbilisi_hotels:
    print(hotel.name)


cheap_rooms = session.query(Room).filter(
    Room.price_per_night < 100
).all()

for room in cheap_rooms:
    print(room.room_number, room.price_per_night)


hotel = get_hotel_by_id(1)

if hotel:
    for room in hotel.rooms:
        print(room.room_number, room.price_per_night)


guest = get_guest_by_email("giorgi@gmail.com")

if guest:
    for booking in guest.bookings:
        print(
            booking.room.room_number,
            booking.check_in,
            booking.check_out
        )


future_bookings = session.query(Booking).filter(
    Booking.check_out > date.today()
).all()

for booking in future_bookings:
    print(
        booking.guest.first_name,
        booking.room.room_number,
        booking.check_out
    )


most_expensive_room = session.query(Room).order_by(
    Room.price_per_night.desc()
).first()

if most_expensive_room:
    print(
        most_expensive_room.room_number,
        most_expensive_room.price_per_night
    )


room_counts = session.query(
    Hotel.name,
    func.count(Room.id)
).join(Room).group_by(Hotel.id).all()

for hotel_name, room_count in room_counts:
    print(hotel_name, room_count, "rooms")


hotels_with_3_rooms = session.query(
    Hotel.name,
    func.count(Room.id)
).join(Room).group_by(
    Hotel.id
).having(
    func.count(Room.id) >= 3
).all()

for hotel_name, room_count in hotels_with_3_rooms:
    print(hotel_name, room_count, "rooms")


guests_with_multiple_bookings = session.query(
    Guest.first_name,
    Guest.last_name,
    func.count(Booking.id)
).join(
    Booking
).group_by(
    Guest.id
).having(
    func.count(Booking.id) > 1
).all()

for first_name, last_name, booking_count in guests_with_multiple_bookings:
    print(first_name, last_name, booking_count, "bookings")


hotel = get_hotel_by_id(1)

if hotel:
    print(hotel.name)

    for room in hotel.rooms:
        print(room.room_number, room.price_per_night)


guest = get_guest_by_email("giorgi@gmail.com")

if guest:
    print(guest.first_name, guest.last_name)

    for booking in guest.bookings:
        print(
            booking.room.room_number,
            booking.room.hotel.name
        )


booking = session.query(Booking).first()

if booking:
    print(booking.guest.first_name)
    print(booking.room.room_number)
    print(booking.room.hotel.name)

